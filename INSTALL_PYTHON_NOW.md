# 🐍 Python Installation Guide - EASY STEPS

## ⚡ Quick Installation (5 Minutes)

### Step 1: Download Python

The Python download page is now open in your browser!

**OR visit:** https://www.python.org/downloads/

### Step 2: Click the Big Yellow Button

Click **"Download Python 3.12.x"** (the big yellow button)

### Step 3: Run the Installer

1. Open the downloaded file (usually in your Downloads folder)
2. **⚠️ MOST IMPORTANT STEP:**

```
┌─────────────────────────────────────────┐
│  Install Python 3.12.x                  │
├─────────────────────────────────────────┤
│                                         │
│  [✓] Add python.exe to PATH  <-- CHECK THIS!
│  [✓] Install pip              <-- CHECK THIS!
│                                         │
│         [ Install Now ]                 │
│                                         │
└─────────────────────────────────────────┘
```

**✅ CHECK both boxes at the bottom!**

3. Click **"Install Now"**
4. Wait for installation (1-2 minutes)
5. Click **"Close"** when done

### Step 4: Verify Installation

1. **Close ALL your terminal windows** (very important!)
2. Open a **NEW** PowerShell or CMD window
3. Type this command:

```powershell
python --version
```

**You should see:** `Python 3.12.x` or similar

4. Also verify pip:

```powershell
pip --version
```

**You should see:** `pip 23.x.x from ...`

---

## ✅ Success! What's Next?

Once you see the Python version, you're ready!

### Run the Automated Setup:

```powershell
# Go to your project folder
cd C:\Users\Umair_Salah\Documents\GitHub\CSV_to_visualization

# Run the setup script
.\setup.ps1
```

This will:
- ✅ Create virtual environment
- ✅ Install all Python packages
- ✅ Install Node.js packages
- ✅ Set up everything automatically

---

## ❌ Troubleshooting

### Problem: Still shows "python is not recognized"

**Solution 1:** Reinstall Python
- Make sure you **CHECK** "Add to PATH" this time!
- Uninstall first: Settings > Apps > Python > Uninstall
- Download and install again

**Solution 2:** Restart your computer
- Sometimes Windows needs a restart to recognize Python

**Solution 3:** Check if Python installed
```powershell
# Check if Python folder exists
Test-Path "C:\Users\$env:USERNAME\AppData\Local\Programs\Python"
```

---

## 📋 After Python is Installed

You also need these (but we can install them later):

### Node.js (for frontend)
- Download: https://nodejs.org/
- Choose LTS version
- Install with default settings

### MySQL (for database)
- Download: https://dev.mysql.com/downloads/installer/
- Choose MySQL Installer
- Install MySQL Server
- Remember your root password!

---

## 🎯 Complete Checklist

- [ ] Install Python (with "Add to PATH" checked) ⚠️ **DO THIS NOW**
- [ ] Close all terminals and open new one
- [ ] Verify: `python --version` works
- [ ] Install Node.js (optional, but needed for frontend)
- [ ] Install MySQL (optional, but needed for database)
- [ ] Run `.\setup.ps1` in project folder

---

## 🚀 Quick Commands After Python Install

```powershell
# 1. Navigate to project
cd C:\Users\Umair_Salah\Documents\GitHub\CSV_to_visualization

# 2. Run automated setup
.\setup.ps1

# 3. Start the application
.\start.ps1
```

---

## 📞 Still Need Help?

The Python download page is open in your browser now.

**Key Points:**
1. ✅ **Check "Add python.exe to PATH"** during installation
2. ✅ **Restart your terminal** after installation
3. ✅ **Verify with:** `python --version`

---

**GO TO YOUR BROWSER NOW** - The Python download page is open!

Click the big yellow "Download Python" button and follow the steps above.
