# Quick Start Guide

## Setup in 5 Minutes

### 1. Database Setup (1 min)
```bash
# Start MySQL and create database
mysql -u root -p
CREATE DATABASE scraper_db;
exit
```

### 2. Backend Setup (2 min)
```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
copy .env.example .env
# Edit .env with your MySQL password
python main.py
```

Backend running at: http://localhost:8000

### 3. Frontend Setup (2 min)
Open new terminal:
```bash
cd frontend
npm install
npm run dev
```

Frontend running at: http://localhost:5173

### 4. Test It Out
1. Open http://localhost:5173
2. Enter URL: `https://ikman.lk/en/ads/sri-lanka/electronics`
3. Click "Run Batch Scraper"
4. View results!

## Common Issues

**Backend won't start:**
- Check if MySQL is running
- Verify DATABASE_URL in `.env`

**Frontend shows errors:**
- Ensure backend is running first
- Check if port 8000 is accessible

**No data scraped:**
- ikman.lk structure may have changed
- Check console for errors
- Update selectors in `scraper.py`

## Next Steps

1. Try the Single Ad Inspector tab
2. Explore the API docs at http://localhost:8000/docs
3. Customize the scraper for other websites
4. Adjust price ranges and charts

Need help? Check the main README.md for detailed documentation.
