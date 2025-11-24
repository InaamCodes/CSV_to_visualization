@echo off
echo Starting Web Scraping Application...
echo.

echo [1/2] Starting Backend (FastAPI)...
cd backend
start cmd /k "python main.py"
cd ..

timeout /t 3 /nobreak > nul

echo [2/2] Starting Frontend (React)...
cd frontend
start cmd /k "npm run dev"
cd ..

echo.
echo ========================================
echo Application is starting!
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173
echo API Docs: http://localhost:8000/docs
echo.
echo Press Ctrl+C in each window to stop
echo ========================================
