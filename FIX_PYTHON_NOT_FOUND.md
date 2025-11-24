# ⚠️ PYTHON NOT INSTALLED - FIX THIS FIRST!

## Your Current Issue

```
'python' is not recognized as an internal or external command
'pip' is not recognized as an internal or external command
```

**This means: Python is NOT installed on your system.**

---

## 🔧 SOLUTION: Install Python (5 minutes)

### Step 1: Download Python

1. **Go to:** https://www.python.org/downloads/
2. **Click:** "Download Python 3.12.x" (big yellow button)
3. **Run the installer**

### Step 2: During Installation - CRITICAL!

⚠️ **IMPORTANT - Don't skip this!**

When the installer opens:
1. ✅ **CHECK the box:** "Add python.exe to PATH" (at the bottom)
2. ✅ **CHECK the box:** "Install pip"
3. Click **"Install Now"**
4. Wait for installation to complete
5. Click **"Close"**

**Screenshot of what to check:**
```
[ ✓ ] Add python.exe to PATH    <--- MUST CHECK THIS!
[ ✓ ] Install pip                <--- MUST CHECK THIS!

        [ Install Now ]
```

### Step 3: Restart Your Terminal

**IMPORTANT:** Close ALL terminal windows and open a NEW one!

### Step 4: Verify Installation

Open a **NEW** PowerShell/CMD window:

```powershell
python --version
```
**Expected output:** `Python 3.12.x` or `Python 3.11.x`

```powershell
pip --version
```
**Expected output:** `pip 23.x.x from ...`

If you see these, **Python is installed correctly!** ✅

---

## ✅ After Python is Installed

Now you can continue with the backend setup:

### Quick Setup (from project root):

```powershell
# Navigate to project root
cd C:\Users\Umair_Salah\Documents\GitHub\CSV_to_visualization

# Go to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# You should see (venv) in your prompt
# (venv) PS C:\...\backend>
```

---

## 🔍 Still Not Working?

### Problem: "python is not recognized" (after installation)

**Cause:** Python not added to PATH during installation

**Solution 1: Reinstall Python**
1. Uninstall Python (Settings > Apps > Python)
2. Download installer again
3. This time, CHECK "Add to PATH" ✅
4. Install again

**Solution 2: Add to PATH manually**
1. Find where Python installed (usually `C:\Python312\`)
2. Open System Environment Variables:
   - Press `Win + X`
   - Click "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find "Path"
   - Click "Edit"
   - Click "New"
   - Add: `C:\Python312\` (adjust version)
   - Add: `C:\Python312\Scripts\`
   - Click OK on all windows
3. Restart terminal

### Problem: Execution policy error (when activating venv)

```powershell
# Run PowerShell as Administrator and execute:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating venv again.

---

## 📦 What About Node.js?

You also need Node.js for the frontend:

### Install Node.js:
1. **Go to:** https://nodejs.org/
2. **Download:** LTS version (18.x or 20.x)
3. **Install** with default settings
4. **Verify:**
   ```powershell
   node --version
   npm --version
   ```

---

## 📦 What About MySQL?

You need MySQL for the database:

### Install MySQL:
1. **Go to:** https://dev.mysql.com/downloads/installer/
2. **Download:** MySQL Installer (Windows)
3. **Install** MySQL Server 8.0+
4. **Set root password** (remember it!)
5. **Start MySQL service**
6. **Create database:**
   ```sql
   mysql -u root -p
   CREATE DATABASE scraper_db;
   exit
   ```

---

## 🎯 Complete Installation Checklist

Run these commands to verify everything:

```powershell
# 1. Check Python
python --version
# Should show: Python 3.11.x or 3.12.x

# 2. Check pip
pip --version
# Should show: pip 23.x.x

# 3. Check Node.js
node --version
# Should show: v18.x.x or v20.x.x

# 4. Check npm
npm --version
# Should show: 9.x.x or 10.x.x

# 5. Check MySQL
mysql -u root -p
# Should connect (enter your password)
```

---

## ✅ All Checks Passed?

Great! Now follow the main installation guide:

```powershell
# Backend setup
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
# Edit .env with your MySQL password
python init_db.py
python main.py
```

```powershell
# Frontend setup (NEW terminal)
cd frontend
npm install
npm run dev
```

**Access your app:**
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 🆘 Quick Links

- **Python Download:** https://www.python.org/downloads/
- **Node.js Download:** https://nodejs.org/
- **MySQL Download:** https://dev.mysql.com/downloads/installer/
- **Full Installation Guide:** See `INSTALLATION.md`

---

## 📞 Next Steps

1. ✅ Install Python (with "Add to PATH" checked)
2. ✅ Install Node.js (LTS version)
3. ✅ Install MySQL (remember root password)
4. ✅ Create database: `CREATE DATABASE scraper_db;`
5. ✅ Update `backend\.env` with MySQL password
6. ✅ Run the setup commands above

---

**REMEMBER:** Always restart your terminal after installing Python!
