from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Dict
from pydantic import BaseModel
from datetime import datetime

from database import get_db, init_db
from models import Product
from scraper import scrape_batch, scrape_single_ad
from config import settings

app = FastAPI(title="Web Scraping & Visualization API")

# CORS middleware to allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class ScrapeBatchRequest(BaseModel):
    url: str
    max_pages: int = None

class ScrapeSingleRequest(BaseModel):
    url: str

class StatsResponse(BaseModel):
    total_items: int
    average_price: float
    items_by_location: List[Dict]
    price_distribution: List[Dict]

@app.on_event("startup")
def startup_event():
    """Initialize database on startup"""
    init_db()
    print("Database initialized!")

@app.get("/")
def read_root():
    return {
        "message": "Web Scraping & Visualization API",
        "endpoints": {
            "POST /api/scrape-batch": "Trigger batch scraping",
            "GET /api/stats": "Get dashboard statistics",
            "POST /api/scrape-single": "Scrape single ad",
            "GET /api/products": "Get all products"
        }
    }

@app.post("/api/scrape-batch")
def scrape_batch_endpoint(request: ScrapeBatchRequest, db: Session = Depends(get_db)):
    """
    Scrape multiple pages and store in database
    """
    try:
        max_pages = request.max_pages if request.max_pages else settings.MAX_PAGES
        
        # Perform batch scraping
        products_data = scrape_batch(request.url, max_pages)
        
        if not products_data:
            return {
                "status": "warning",
                "message": "No products found",
                "scraped_count": 0
            }
        
        # Store or update products in database
        added_count = 0
        updated_count = 0
        
        for product_data in products_data:
            # Check if product already exists by link
            existing_product = db.query(Product).filter(Product.link == product_data['link']).first()
            
            if existing_product:
                # Update existing product
                existing_product.title = product_data['title']
                existing_product.price = product_data['price']
                existing_product.location = product_data['location']
                existing_product.posted_time = product_data['posted_time']
                existing_product.image_url = product_data['image_url']
                existing_product.scraped_at = datetime.utcnow()
                updated_count += 1
            else:
                # Add new product
                new_product = Product(
                    title=product_data['title'],
                    price=product_data['price'],
                    location=product_data['location'],
                    posted_time=product_data['posted_time'],
                    link=product_data['link'],
                    image_url=product_data['image_url']
                )
                db.add(new_product)
                added_count += 1
        
        db.commit()
        
        return {
            "status": "success",
            "message": f"Scraping completed. Added {added_count} new items, updated {updated_count} items.",
            "scraped_count": len(products_data),
            "added": added_count,
            "updated": updated_count
        }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error during scraping: {str(e)}")

@app.get("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    """
    Get statistics for dashboard
    """
    try:
        # Total items
        total_items = db.query(func.count(Product.id)).scalar()
        
        # Average price (excluding None values)
        avg_price_result = db.query(func.avg(Product.price)).filter(Product.price.isnot(None)).scalar()
        average_price = float(avg_price_result) if avg_price_result else 0.0
        
        # Items by location
        items_by_location = db.query(
            Product.location,
            func.count(Product.id).label('count')
        ).group_by(Product.location).all()
        
        items_by_location_list = [
            {"location": loc or "Unknown", "count": count}
            for loc, count in items_by_location
        ]
        
        # Price distribution (grouping by price ranges)
        price_ranges = [
            {"range": "0-10k", "min": 0, "max": 10000},
            {"range": "10k-50k", "min": 10000, "max": 50000},
            {"range": "50k-100k", "min": 50000, "max": 100000},
            {"range": "100k-500k", "min": 100000, "max": 500000},
            {"range": "500k+", "min": 500000, "max": 999999999},
        ]
        
        price_distribution = []
        for range_info in price_ranges:
            count = db.query(func.count(Product.id)).filter(
                Product.price >= range_info['min'],
                Product.price < range_info['max']
            ).scalar()
            
            if count > 0:
                price_distribution.append({
                    "range": range_info['range'],
                    "count": count
                })
        
        return {
            "total_items": total_items,
            "average_price": round(average_price, 2),
            "items_by_location": items_by_location_list,
            "price_distribution": price_distribution
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching stats: {str(e)}")

@app.post("/api/scrape-single")
def scrape_single_endpoint(request: ScrapeSingleRequest):
    """
    Scrape a single ad page and return detailed information
    """
    try:
        product_data = scrape_single_ad(request.url)
        
        if not product_data:
            raise HTTPException(status_code=404, detail="Failed to scrape the provided URL. Please check if the URL is valid.")
        
        return {
            "status": "success",
            "data": product_data
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error scraping ad: {str(e)}")

@app.get("/api/products")
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all products from database with pagination
    """
    try:
        products = db.query(Product).order_by(Product.scraped_at.desc()).offset(skip).limit(limit).all()
        
        return {
            "status": "success",
            "data": [product.to_dict() for product in products],
            "count": len(products)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching products: {str(e)}")

@app.delete("/api/products/clear")
def clear_products(db: Session = Depends(get_db)):
    """
    Clear all products from database (useful for testing)
    """
    try:
        deleted_count = db.query(Product).delete()
        db.commit()
        
        return {
            "status": "success",
            "message": f"Deleted {deleted_count} products",
            "deleted_count": deleted_count
        }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error clearing products: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
