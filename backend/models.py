from sqlalchemy import Column, Integer, String, Numeric, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    price = Column(Numeric(10, 2), nullable=True)
    location = Column(String(200), nullable=True)
    posted_time = Column(String(100), nullable=True)
    link = Column(String(1000), unique=True, nullable=False)
    image_url = Column(String(1000), nullable=True)
    scraped_at = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": float(self.price) if self.price else None,
            "location": self.location,
            "posted_time": self.posted_time,
            "link": self.link,
            "image_url": self.image_url,
            "scraped_at": self.scraped_at.isoformat() if self.scraped_at else None
        }
