@echo off
cd /d "%~dp0"
cd app\.. 
call venv\Scripts\activate.bat
python -m uvicorn app.main:app --reload
pause
