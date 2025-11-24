from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:password@localhost:3306/scraper_db"
    MAX_PAGES: int = 5
    
    class Config:
        env_file = ".env"

settings = Settings()
