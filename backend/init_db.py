"""
Database initialization script
Run this to create tables in your MySQL database
"""

from database import init_db
from config import settings

if __name__ == "__main__":
    print("Initializing database...")
    print(f"Database URL: {settings.DATABASE_URL}")
    
    try:
        init_db()
        print("✓ Database tables created successfully!")
        print("✓ Ready to start scraping!")
    except Exception as e:
        print(f"✗ Error initializing database: {e}")
        print("\nPlease check:")
        print("1. MySQL server is running")
        print("2. Database exists (CREATE DATABASE scraper_db;)")
        print("3. Credentials in .env file are correct")
