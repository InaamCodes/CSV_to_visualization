# Automated Setup Script for Web Scraping Application
# Run this AFTER installing Python, Node.js, and MySQL

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Web Scraping App - Setup Script" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check prerequisites
Write-Host "[1/5] Checking prerequisites..." -ForegroundColor Yellow

# Check Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  ✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Python not found!" -ForegroundColor Red
    Write-Host "  Please install Python from: https://www.python.org/downloads/" -ForegroundColor Red
    Write-Host "  Make sure to check 'Add to PATH' during installation!" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit
}

# Check Node.js
try {
    $nodeVersion = node --version 2>&1
    Write-Host "  ✓ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Node.js not found!" -ForegroundColor Red
    Write-Host "  Please install Node.js from: https://nodejs.org/" -ForegroundColor Red
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit
}

# Check MySQL
Write-Host "  ℹ MySQL check skipped (will verify when starting backend)" -ForegroundColor Cyan

Write-Host ""
Write-Host "[2/5] Setting up Python backend..." -ForegroundColor Yellow
Set-Location backend

# Create virtual environment
if (-Not (Test-Path "venv")) {
    Write-Host "  Creating virtual environment..." -ForegroundColor Cyan
    python -m venv venv
    Write-Host "  ✓ Virtual environment created" -ForegroundColor Green
} else {
    Write-Host "  ✓ Virtual environment already exists" -ForegroundColor Green
}

# Activate virtual environment and install dependencies
Write-Host "  Installing Python dependencies..." -ForegroundColor Cyan
& ".\venv\Scripts\pip.exe" install -r requirements.txt
Write-Host "  ✓ Python dependencies installed" -ForegroundColor Green

# Check if .env exists
if (-Not (Test-Path ".env")) {
    Write-Host "  ⚠ .env file not found!" -ForegroundColor Yellow
    Write-Host "  Copying .env.example to .env..." -ForegroundColor Cyan
    Copy-Item ".env.example" ".env"
    Write-Host "  ✓ .env file created" -ForegroundColor Green
    Write-Host "  ⚠ IMPORTANT: Edit backend\.env with your MySQL password!" -ForegroundColor Yellow
} else {
    Write-Host "  ✓ .env file exists" -ForegroundColor Green
}

Set-Location ..

Write-Host ""
Write-Host "[3/5] Setting up React frontend..." -ForegroundColor Yellow
Set-Location frontend

Write-Host "  Installing Node.js dependencies..." -ForegroundColor Cyan
npm install
Write-Host "  ✓ Node.js dependencies installed" -ForegroundColor Green

Set-Location ..

Write-Host ""
Write-Host "[4/5] Initializing database..." -ForegroundColor Yellow
Write-Host "  Make sure MySQL is running and database 'scraper_db' exists!" -ForegroundColor Cyan

$initDb = Read-Host "  Do you want to initialize the database now? (y/n)"
if ($initDb -eq "y" -or $initDb -eq "Y") {
    Set-Location backend
    & ".\venv\Scripts\python.exe" init_db.py
    Set-Location ..
} else {
    Write-Host "  Skipped. Run 'python init_db.py' manually later." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "[5/5] Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  🎉 Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Make sure MySQL is running" -ForegroundColor White
Write-Host "  2. Edit backend\.env with your MySQL password" -ForegroundColor White
Write-Host "  3. Create database: CREATE DATABASE scraper_db;" -ForegroundColor White
Write-Host "  4. Run the application:" -ForegroundColor White
Write-Host ""
Write-Host "     .\start.ps1" -ForegroundColor Cyan
Write-Host ""
Write-Host "Or start manually:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  Terminal 1 (Backend):" -ForegroundColor White
Write-Host "    cd backend" -ForegroundColor Gray
Write-Host "    .\venv\Scripts\Activate.ps1" -ForegroundColor Gray
Write-Host "    python main.py" -ForegroundColor Gray
Write-Host ""
Write-Host "  Terminal 2 (Frontend):" -ForegroundColor White
Write-Host "    cd frontend" -ForegroundColor Gray
Write-Host "    npm run dev" -ForegroundColor Gray
Write-Host ""
Write-Host "Access your application:" -ForegroundColor Yellow
Write-Host "  Frontend:  http://localhost:5173" -ForegroundColor Cyan
Write-Host "  Backend:   http://localhost:8000" -ForegroundColor Cyan
Write-Host "  API Docs:  http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Enter to exit..." -ForegroundColor Gray
Read-Host
