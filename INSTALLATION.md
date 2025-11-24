# ⚡ Installation Guide - Step by Step

Follow these steps carefully to get your application running.

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] **Python 3.8 or higher** installed
  - Check: Open PowerShell and run `python --version`
  - Download: https://www.python.org/downloads/
  
- [ ] **Node.js 16 or higher** installed
  - Check: `node --version`
  - Download: https://nodejs.org/
  
- [ ] **MySQL 8.0 or higher** installed and running
  - Check: `mysql --version`
  - Download: https://dev.mysql.com/downloads/installer/
  
- [ ] **Git** (optional, for version control)
  - Check: `git --version`
  - Download: https://git-scm.com/

---

## 🗄️ Step 1: MySQL Database Setup

### 1.1 Start MySQL Service
```powershell
# Check if MySQL is running
Get-Service -Name MySQL* | Select-Object Name, Status

# If not running, start it
Start-Service -Name MySQL80  # Adjust name if needed
```

### 1.2 Access MySQL
```powershell
mysql -u root -p
# Enter your root password when prompted
```

### 1.3 Create Database
```sql
CREATE DATABASE scraper_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Verify database was created
SHOW DATABASES;

-- Optional: Create dedicated user
CREATE USER 'scraper_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON scraper_db.* TO 'scraper_user'@'localhost';
FLUSH PRIVILEGES;

-- Exit MySQL
EXIT;
```

✅ **Database Setup Complete!**

---

## 🐍 Step 2: Backend Setup (Python/FastAPI)

### 2.1 Navigate to Backend Directory
```powershell
cd c:\Users\Umair_Salah\Documents\GitHub\CSV_to_visualization\backend
```

### 2.2 Create Virtual Environment
```powershell
# Create venv
python -m venv venv

# If you get an error, try:
python3 -m venv venv
```

### 2.3 Activate Virtual Environment
```powershell
# PowerShell (Recommended)
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# CMD (Alternative)
# venv\Scripts\activate.bat
```

You should see `(venv)` in your prompt.

### 2.4 Install Dependencies
```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt

# This will install:
# - fastapi
# - uvicorn
# - sqlalchemy
# - pymysql
# - beautifulsoup4
# - requests
# - python-dotenv
# - pydantic
```

### 2.5 Configure Environment Variables
```powershell
# Copy the example file
copy .env.example .env

# Edit .env file with your credentials
notepad .env
```

**Edit these values in .env:**
```env
DATABASE_URL=mysql+pymysql://root:YOUR_MYSQL_PASSWORD@localhost:3306/scraper_db
MAX_PAGES=5
```

Replace `YOUR_MYSQL_PASSWORD` with your actual MySQL password.

### 2.6 Initialize Database
```powershell
# Create tables
python init_db.py

# You should see:
# Initializing database...
# ✓ Database tables created successfully!
```

### 2.7 Test Backend
```powershell
# Start the server
python main.py

# You should see:
# INFO:     Uvicorn running on http://0.0.0.0:8000
# INFO:     Application startup complete.
```

**Test in browser:** http://localhost:8000

You should see:
```json
{
  "message": "Web Scraping & Visualization API",
  "endpoints": {...}
}
```

✅ **Backend Setup Complete!**

**Keep this terminal open and running.**

---

## ⚛️ Step 3: Frontend Setup (React/Vite)

### 3.1 Open New Terminal
Open a **new PowerShell terminal** (keep backend running in the first one)

### 3.2 Navigate to Frontend Directory
```powershell
cd c:\Users\Umair_Salah\Documents\GitHub\CSV_to_visualization\frontend
```

### 3.3 Install Node Dependencies
```powershell
# Install all packages (this may take 2-3 minutes)
npm install

# This will install:
# - react & react-dom
# - vite
# - tailwindcss
# - chart.js
# - axios
# - react-router-dom
# - And all their dependencies
```

### 3.4 Start Development Server
```powershell
npm run dev

# You should see:
#   VITE v5.0.0  ready in 500 ms
#   ➜  Local:   http://localhost:5173/
#   ➜  Network: use --host to expose
```

✅ **Frontend Setup Complete!**

**Keep this terminal open too.**

---

## 🌐 Step 4: Access Your Application

### 4.1 Open Browser
Open your web browser and go to:

**http://localhost:5173**

You should see the beautiful dashboard! 🎉

### 4.2 Test the Application

**Option A: Batch Scraper**
1. You'll see the Dashboard page
2. In the URL field, enter:
   ```
   https://ikman.lk/en/ads/sri-lanka/electronics
   ```
3. Set Max Pages to: `2` (start small)
4. Click **"Run Batch Scraper"**
5. Wait 30-60 seconds
6. See the results populate!

**Option B: Single Ad Inspector**
1. Click **"Ad Inspector"** tab
2. Find any ikman.lk ad (e.g., search for "iPhone" on ikman.lk)
3. Copy the ad URL
4. Paste it in the input
5. Click **"Analyze Ad"**
6. See the beautiful product card!

---

## 🎯 Verification Checklist

After setup, verify everything is working:

### Backend Verification
- [ ] Terminal shows "Uvicorn running"
- [ ] http://localhost:8000 shows API info
- [ ] http://localhost:8000/docs shows Swagger UI

### Frontend Verification
- [ ] Terminal shows "VITE ready"
- [ ] http://localhost:5173 shows dashboard
- [ ] Navigation works (Dashboard ↔ Ad Inspector)

### Database Verification
```powershell
# In MySQL
mysql -u root -p
USE scraper_db;
SHOW TABLES;  # Should show 'products' table
```

### Integration Verification
- [ ] Can scrape data (batch scraper works)
- [ ] Charts display correctly
- [ ] Products appear in table
- [ ] Single ad analyzer works

---

## 🔧 Troubleshooting

### Issue: Python not found
**Solution:**
```powershell
# Add Python to PATH or use full path
C:\Python3X\python.exe -m venv venv
```

### Issue: Can't activate virtual environment
**Solution:**
```powershell
# Enable script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Then try again
.\venv\Scripts\Activate.ps1
```

### Issue: MySQL connection error
**Solutions:**
1. Check MySQL is running:
   ```powershell
   Get-Service -Name MySQL*
   ```
2. Verify password in `.env` file
3. Test connection:
   ```powershell
   mysql -u root -p
   ```
4. Check DATABASE_URL format in `.env`

### Issue: Port already in use
**Solution:**
```powershell
# Check what's using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID with actual number)
taskkill /PID <PID> /F

# Or use different port in main.py:
# uvicorn.run(app, host="0.0.0.0", port=8001)
```

### Issue: npm install fails
**Solutions:**
1. Clear npm cache:
   ```powershell
   npm cache clean --force
   ```
2. Delete node_modules and try again:
   ```powershell
   Remove-Item -Recurse -Force node_modules
   npm install
   ```
3. Update npm:
   ```powershell
   npm install -g npm@latest
   ```

### Issue: Frontend can't connect to backend
**Check:**
1. Backend is running on port 8000
2. No firewall blocking localhost
3. Check `frontend/src/api.js` - should be:
   ```javascript
   const API_BASE_URL = 'http://localhost:8000';
   ```

### Issue: No data appears after scraping
**Solutions:**
1. Check backend terminal for errors
2. Check browser console (F12)
3. Verify ikman.lk URL is correct
4. Try the API directly:
   ```powershell
   curl http://localhost:8000/api/stats
   ```

---

## 🚀 Quick Start Scripts

### Method 1: PowerShell Script (Easiest)
```powershell
cd c:\Users\Umair_Salah\Documents\GitHub\CSV_to_visualization
.\start.ps1
```

### Method 2: Manual in 2 Terminals
**Terminal 1 (Backend):**
```powershell
cd c:\Users\Umair_Salah\Documents\GitHub\CSV_to_visualization\backend
.\venv\Scripts\Activate.ps1
python main.py
```

**Terminal 2 (Frontend):**
```powershell
cd c:\Users\Umair_Salah\Documents\GitHub\CSV_to_visualization\frontend
npm run dev
```

---

## 📊 Testing the Installation

### Test 1: API Health Check
```powershell
curl http://localhost:8000
# Should return JSON with API info
```

### Test 2: Swagger UI
Open: http://localhost:8000/docs
- Try the `/api/stats` endpoint
- Should return current statistics

### Test 3: Frontend Loading
Open: http://localhost:5173
- Dashboard should load
- Navigation should work
- No console errors (F12)

### Test 4: End-to-End Scraping
1. Go to http://localhost:5173
2. Enter URL: `https://ikman.lk/en/ads/sri-lanka/mobile-phones`
3. Set pages: `1`
4. Click "Run Batch Scraper"
5. Wait for completion
6. Check if data appears in table

---

## 🎓 Understanding Your Setup

### What's Running Where?

| Service | Port | URL | Purpose |
|---------|------|-----|---------|
| Backend API | 8000 | http://localhost:8000 | FastAPI server |
| Frontend | 5173 | http://localhost:5173 | React dev server |
| MySQL | 3306 | localhost:3306 | Database |
| API Docs | 8000 | http://localhost:8000/docs | Swagger UI |

### File Structure You Created

```
✓ backend/venv/          # Python virtual environment
✓ backend/.env           # Your database credentials
✓ frontend/node_modules/ # Node.js dependencies
✓ Database: scraper_db   # MySQL database with products table
```

---

## 🔄 Daily Usage

### Starting the Application
```powershell
# Quick method
.\start.ps1

# Or manually start both servers as shown above
```

### Stopping the Application
```
Press Ctrl+C in each terminal window
```

### Updating Dependencies

**Backend:**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt --upgrade
```

**Frontend:**
```powershell
cd frontend
npm update
```

---

## ✅ Installation Complete!

If you've followed all steps, you now have:

- ✅ MySQL database running
- ✅ Python backend with FastAPI
- ✅ React frontend with Vite
- ✅ All dependencies installed
- ✅ Database tables created
- ✅ Application running and tested

### Next Steps:

1. **Read** the main README.md for detailed features
2. **Explore** the API at http://localhost:8000/docs
3. **Try** scraping different ikman.lk categories
4. **Customize** the code to your needs

---

## 📞 Getting Help

If you encounter issues:

1. Check this installation guide
2. See README.md troubleshooting section
3. Check terminal output for error messages
4. Verify all prerequisites are met
5. Try the troubleshooting steps above

---

**Congratulations! Your Web Scraping Application is Ready!** 🎉

Start scraping and analyzing ikman.lk data! 🚀
