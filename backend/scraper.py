import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import re

def extract_price(price_text: str) -> Optional[float]:
    """Extract numeric price from text like 'Rs 50,000' or 'Rs 1,500'"""
    if not price_text:
        return None
    
    # Remove 'Rs' and commas, then convert to float
    price_cleaned = re.sub(r'[Rs,\s]', '', price_text)
    try:
        return float(price_cleaned)
    except ValueError:
        return None

def scrape_ikman_page(url: str) -> List[Dict]:
    """
    Scrape a single ikman.lk search results page
    Returns a list of product dictionaries
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        # Find all ad listings - adjust selectors based on ikman.lk structure
        ads = soup.find_all('li', class_='normal--2QYVk')
        
        for ad in ads:
            try:
                # Extract title
                title_elem = ad.find('h2')
                title = title_elem.get_text(strip=True) if title_elem else "N/A"
                
                # Extract price
                price_elem = ad.find('div', class_='price--3SnqI')
                price_text = price_elem.get_text(strip=True) if price_elem else None
                price = extract_price(price_text) if price_text else None
                
                # Extract location
                location_elem = ad.find('div', class_='description--1nRbz')
                location = location_elem.get_text(strip=True) if location_elem else "N/A"
                
                # Extract posted time
                time_elem = ad.find('div', class_='updated-time--1DbCk')
                posted_time = time_elem.get_text(strip=True) if time_elem else "N/A"
                
                # Extract link
                link_elem = ad.find('a', href=True)
                link = "https://ikman.lk" + link_elem['href'] if link_elem else None
                
                # Extract image
                img_elem = ad.find('img')
                image_url = img_elem.get('src') or img_elem.get('data-src') if img_elem else None
                
                if title and link:
                    products.append({
                        'title': title,
                        'price': price,
                        'location': location,
                        'posted_time': posted_time,
                        'link': link,
                        'image_url': image_url
                    })
            except Exception as e:
                print(f"Error parsing ad: {e}")
                continue
        
        return products
    
    except Exception as e:
        print(f"Error scraping page {url}: {e}")
        return []

def scrape_batch(base_url: str, max_pages: int = 5) -> List[Dict]:
    """
    Scrape multiple pages from ikman.lk
    """
    all_products = []
    
    for page_num in range(1, max_pages + 1):
        # Construct page URL (adjust based on ikman.lk pagination)
        if page_num == 1:
            page_url = base_url
        else:
            # ikman.lk typically uses ?page=2, ?page=3, etc.
            separator = '&' if '?' in base_url else '?'
            page_url = f"{base_url}{separator}page={page_num}"
        
        print(f"Scraping page {page_num}: {page_url}")
        products = scrape_ikman_page(page_url)
        all_products.extend(products)
        
        if not products:
            print(f"No products found on page {page_num}, stopping...")
            break
    
    return all_products

def scrape_single_ad(url: str) -> Optional[Dict]:
    """
    Scrape detailed information from a single ad page
    Returns detailed product information including description
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title_elem = soup.find('h1', class_='title--3s1R8')
        title = title_elem.get_text(strip=True) if title_elem else "N/A"
        
        # Extract price
        price_elem = soup.find('div', class_='amount--3NTpl')
        price_text = price_elem.get_text(strip=True) if price_elem else None
        price = extract_price(price_text) if price_text else None
        
        # Extract description
        desc_elem = soup.find('div', class_='description--1nRbz')
        description = desc_elem.get_text(strip=True) if desc_elem else "No description available"
        
        # Extract location
        location_elem = soup.find('div', attrs={'data-testid': 'ad-location'})
        location = location_elem.get_text(strip=True) if location_elem else "N/A"
        
        # Extract images
        images = []
        img_container = soup.find('div', class_='image-container--30CXk')
        if img_container:
            img_elems = img_container.find_all('img')
            images = [img.get('src') or img.get('data-src') for img in img_elems if img.get('src') or img.get('data-src')]
        
        # Extract seller name
        seller_elem = soup.find('div', class_='seller-name--2ZfVu')
        seller_name = seller_elem.get_text(strip=True) if seller_elem else "Unknown Seller"
        
        return {
            'title': title,
            'price': price,
            'description': description,
            'location': location,
            'images': images,
            'seller_name': seller_name,
            'url': url
        }
    
    except Exception as e:
        print(f"Error scraping single ad {url}: {e}")
        return None
