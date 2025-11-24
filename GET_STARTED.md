# 🚀 Complete Web Scraping & Visualization Application

## Your application has been successfully built!

This is a **production-ready** full-stack application for scraping ikman.lk with advanced features:

---

## 📂 Project Structure

```
CSV_to_visualization/
│
├── 📁 backend/                          # Python FastAPI Backend
│   ├── main.py                          # FastAPI app with all endpoints
│   ├── models.py                        # SQLAlchemy Product model
│   ├── database.py                      # Database connection & sessions
│   ├── scraper.py                       # Web scraping logic (BeautifulSoup)
│   ├── config.py                        # Settings & environment config
│   ├── init_db.py                       # Database initialization script
│   ├── requirements.txt                 # Python dependencies
│   ├── .env.example                     # Environment variables template
│   └── .env                             # Your environment config
│
├── 📁 frontend/                         # React + Vite Frontend
│   ├── 📁 src/
│   │   ├── 📁 pages/
│   │   │   ├── Dashboard.jsx            # Main dashboard with charts
│   │   │   └── SingleAdInspector.jsx   # Single ad analyzer
│   │   ├── App.jsx                      # Main app with routing
│   │   ├── api.js                       # Axios API client
│   │   ├── main.jsx                     # React entry point
│   │   └── index.css                    # Tailwind CSS
│   ├── index.html                       # HTML template
│   ├── package.json                     # NPM dependencies
│   ├── vite.config.js                   # Vite configuration
│   ├── tailwind.config.js               # Tailwind configuration
│   └── postcss.config.js                # PostCSS configuration
│
├── 📄 README.md                         # Complete documentation (400+ lines)
├── 📄 QUICKSTART.md                     # 5-minute setup guide
├── 📄 PROJECT_SUMMARY.md                # This file - project overview
├── 📄 .gitignore                        # Git ignore rules
├── 🚀 start.ps1                         # PowerShell startup script
└── 🚀 start.bat                         # Windows batch startup script
```

---

## 🎯 What Can This Application Do?

### 1. **Batch Scraper Dashboard** 📊
- Input any ikman.lk search URL
- Scrape 1-10 pages of results
- Store all data in MySQL database
- View statistics:
  - **Total items scraped**
  - **Average price**
- Interactive charts:
  - **Bar Chart:** Items per location (e.g., Colombo vs Kandy)
  - **Line Chart:** Price distribution across ranges
- **Data table** showing all products with:
  - Thumbnails
  - Title, price, location
  - Posted time
  - Direct links
- Automatic deduplication (won't create duplicates)

### 2. **Single Ad Inspector** 🔍
- Paste any ikman.lk ad URL
- Get instant detailed analysis
- Beautiful **Product Card** showing:
  - **Image Gallery** with thumbnail navigation
  - **Huge price display** (Rs 250,000 style)
  - **Location badge** with icon
  - **Seller information**
  - **Full description**
  - Link to original ad

### 3. **RESTful API** 🌐
- **5 endpoints** ready to use
- Auto-generated **Swagger documentation**
- CORS enabled for frontend
- Proper error handling
- Pagination support

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | FastAPI | Modern Python web framework |
| | SQLAlchemy | Database ORM |
| | BeautifulSoup4 | Web scraping |
| | PyMySQL | MySQL connector |
| | Pydantic | Data validation |
| **Frontend** | React 18 | UI framework |
| | Vite | Build tool (super fast) |
| | Tailwind CSS | Styling |
| | Chart.js | Data visualization |
| | Axios | HTTP requests |
| | React Router | Navigation |
| **Database** | MySQL 8.0+ | Relational database |

---

## 🚀 Quick Start (3 Steps)

### Step 1: Setup MySQL
```sql
CREATE DATABASE scraper_db;
```

### Step 2: Configure Backend
Edit `backend/.env`:
```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/scraper_db
MAX_PAGES=5
```

### Step 3: Run Everything
```powershell
# Option A: Automated (Recommended)
.\start.ps1

# Option B: Manual
# Terminal 1
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py

# Terminal 2
cd frontend
npm install
npm run dev
```

### Access Your Application
- 🌐 **Frontend:** http://localhost:5173
- 🔌 **Backend API:** http://localhost:8000
- 📚 **API Docs:** http://localhost:8000/docs

---

## 📖 Usage Examples

### Example 1: Scrape Electronics
1. Go to http://localhost:5173
2. Enter: `https://ikman.lk/en/ads/sri-lanka/electronics`
3. Set pages: `3`
4. Click **"Run Batch Scraper"**
5. Wait 30-60 seconds
6. View results: charts, stats, and table!

### Example 2: Analyze Single Ad
1. Click **"Ad Inspector"** tab
2. Paste: `https://ikman.lk/en/ad/apple-iphone-13-pro-max-...`
3. Click **"Analyze Ad"**
4. See beautiful product card with all details!

### Example 3: Use API Directly
```bash
# Scrape batch
curl -X POST http://localhost:8000/api/scrape-batch \
  -H "Content-Type: application/json" \
  -d '{"url": "https://ikman.lk/en/ads/sri-lanka/electronics", "max_pages": 3}'

# Get stats
curl http://localhost:8000/api/stats

# Scrape single
curl -X POST http://localhost:8000/api/scrape-single \
  -H "Content-Type: application/json" \
  -d '{"url": "https://ikman.lk/en/ad/..."}'
```

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/api/scrape-batch` | POST | Scrape multiple pages |
| `/api/stats` | GET | Dashboard statistics |
| `/api/scrape-single` | POST | Analyze single ad |
| `/api/products` | GET | Get all products (paginated) |
| `/api/products/clear` | DELETE | Clear database |

**Interactive Documentation:** http://localhost:8000/docs

---

## ✨ Key Features

### Smart Scraping
- ✅ Handles pagination automatically
- ✅ Extracts: title, price, location, time, images, links
- ✅ Works with ikman.lk HTML structure
- ✅ Error handling for missing data
- ✅ Retries and timeouts

### Database
- ✅ MySQL with SQLAlchemy ORM
- ✅ Automatic table creation
- ✅ Deduplication by link
- ✅ Update existing entries
- ✅ Timestamp tracking

### Frontend
- ✅ Modern, responsive design
- ✅ Mobile-friendly
- ✅ Real-time updates
- ✅ Loading states
- ✅ Error messages
- ✅ Chart interactions
- ✅ Image galleries

### Code Quality
- ✅ Modular architecture
- ✅ Type hints (Python)
- ✅ Environment variables
- ✅ Error handling
- ✅ Code comments
- ✅ Reusable components

---

## 🎨 Screenshots (What You'll See)

### Dashboard View
```
┌─────────────────────────────────────────────────┐
│  📊 Batch Scraper Dashboard                    │
├─────────────────────────────────────────────────┤
│  URL: [https://ikman.lk/en/ads/sri-lanka/...] │
│  Max Pages: [5]        [🚀 Run Batch Scraper]  │
├─────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐             │
│  │ Total: 150  │  │ Avg: Rs 45K │             │
│  └─────────────┘  └─────────────┘             │
├─────────────────────────────────────────────────┤
│  📊 Items by Location  │  📈 Price Distribution│
│  [Bar Chart]           │  [Line Chart]         │
├─────────────────────────────────────────────────┤
│  Table: Title | Price | Location | Action      │
│  ─────────────────────────────────────────────  │
│  [img] iPhone 13 | Rs 250K | Colombo | View →  │
│  [img] Samsung   | Rs 150K | Kandy   | View →  │
└─────────────────────────────────────────────────┘
```

### Ad Inspector View
```
┌─────────────────────────────────────────────────┐
│  🔍 Single Ad Inspector                        │
├─────────────────────────────────────────────────┤
│  URL: [https://ikman.lk/en/ad/...]            │
│  [🔍 Analyze Ad]                               │
├─────────────────────────────────────────────────┤
│  ┌──────────┐  │  iPhone 13 Pro Max          │
│  │  [IMG]   │  │  Rs 250,000                 │
│  │  [][][]  │  │  📍 Colombo 3               │
│  └──────────┘  │  👤 John Doe                │
│                │  Description: ...             │
│                │  [View on ikman.lk →]        │
└─────────────────────────────────────────────────┘
```

---

## 🔧 Customization

### Change Scraping Target
Edit `backend/scraper.py` - Lines 40-70:
```python
ads = soup.find_all('li', class_='normal--2QYVk')  # Your selector
title_elem = ad.find('h2')  # Your element
```

### Modify Price Ranges
Edit `backend/main.py` - Lines 120-130:
```python
price_ranges = [
    {"range": "0-10k", "min": 0, "max": 10000},
    # Add your ranges...
]
```

### Change Colors
Edit `frontend/tailwind.config.js`:
```javascript
colors: {
  primary: {
    500: '#0ea5e9',  // Your color
  }
}
```

---

## 📚 Documentation Files

1. **README.md** - Full documentation (setup, API, troubleshooting)
2. **QUICKSTART.md** - 5-minute setup guide
3. **PROJECT_SUMMARY.md** - This file
4. **API Docs** - http://localhost:8000/docs (when running)

---

## 🐛 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Backend won't start | Check MySQL is running, verify .env credentials |
| Frontend shows errors | Ensure backend runs first on port 8000 |
| No data scraped | ikman.lk structure changed - update selectors |
| Charts not showing | Run `npm install` in frontend directory |
| Import errors | Activate virtual environment |

**See README.md for detailed troubleshooting.**

---

## 🎓 Learning Resources

### Understanding the Code
1. **FastAPI:** https://fastapi.tiangolo.com/
2. **React:** https://react.dev/
3. **SQLAlchemy:** https://docs.sqlalchemy.org/
4. **BeautifulSoup:** https://www.crummy.com/software/BeautifulSoup/
5. **Tailwind CSS:** https://tailwindcss.com/

### Extending the Application
- Add authentication (JWT tokens)
- Deploy to cloud (AWS, Heroku, Vercel)
- Add more scrapers (other websites)
- Implement scheduling (celery)
- Add export features (CSV, PDF)

---

## 📦 What's Included

### Backend Files (8 files)
- ✅ Complete FastAPI application
- ✅ Database models and migrations
- ✅ Web scraping logic
- ✅ Configuration management
- ✅ Requirements and setup

### Frontend Files (11 files)
- ✅ React application with routing
- ✅ Two complete pages
- ✅ API client integration
- ✅ Tailwind CSS styling
- ✅ Chart.js visualizations

### Documentation (4 files)
- ✅ Comprehensive README
- ✅ Quick start guide
- ✅ Project summary
- ✅ Auto-generated API docs

### Utilities (3 files)
- ✅ PowerShell start script
- ✅ Batch start script
- ✅ Git ignore file

**Total: 26 files carefully crafted for you!**

---

## 🎯 Next Steps

### 1. Initial Setup (10 min)
- [ ] Install MySQL
- [ ] Create database
- [ ] Update .env file
- [ ] Install Python dependencies
- [ ] Install Node dependencies

### 2. First Run (2 min)
- [ ] Start backend
- [ ] Start frontend
- [ ] Open browser
- [ ] Test scraping

### 3. Explore Features (10 min)
- [ ] Try batch scraper
- [ ] View charts
- [ ] Use ad inspector
- [ ] Check API docs

### 4. Customize (Optional)
- [ ] Change colors
- [ ] Modify price ranges
- [ ] Add more charts
- [ ] Extend database model

---

## 💡 Pro Tips

1. **Use the API docs** at /docs to test endpoints interactively
2. **Start small** - scrape 1-2 pages first to test
3. **Monitor logs** in the terminal for debugging
4. **Use the inspector** to understand ikman.lk structure
5. **Backup database** before clearing products

---

## 🎉 You're Ready!

Your complete web scraping application is ready to use!

**Quick Commands:**
```powershell
# Start everything
.\start.ps1

# Or manually
cd backend; python main.py
cd frontend; npm run dev
```

**Access:**
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 📞 Need Help?

1. Check **README.md** for detailed docs
2. See **QUICKSTART.md** for fast setup
3. Visit **http://localhost:8000/docs** for API reference
4. Review error messages in terminal
5. Check browser console (F12)

---

## ✅ Checklist Before Running

- [ ] MySQL installed and running
- [ ] Database `scraper_db` created
- [ ] Python 3.8+ installed
- [ ] Node.js 16+ installed
- [ ] `.env` file configured
- [ ] Port 8000 available
- [ ] Port 5173 available

**If all checked, you're good to go!** 🚀

---

**Built with ❤️ for your ikman.lk scraping needs**

*Happy Scraping!* 🎉
