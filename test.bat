@echo off
REM ============================
REM Run Python script and open browser (Fixed)
REM ============================

echo Starting test.py in new terminal...
start "" cmd /c "python test.py"

echo Waiting for server to start...
timeout /t 5 >nul

echo Opening http://127.0.0.1:10000
start http://127.0.0.1:10000

pause
