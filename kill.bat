@echo off

REM Check if running with administrative privileges
NET SESSION >nul 2>&1
if %errorlevel% neq 0 (
    echo This script requires administrative privileges.
    echo Please right-click the batch file and select "Run as administrator."
    pause
    exit /b
)

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not found on this computer.
    echo Please download and install Python from the official website.
    start "" "https://www.python.org/downloads/"
    pause
    exit /b
)

REM Python is found
echo OK

REM Install required libraries
pip install psutil

python kill.py
pause
