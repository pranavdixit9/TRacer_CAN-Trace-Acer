@echo off
cd /d %~dp0
cd ..

echo --------------------------------------------
echo [1/5] Creating virtual environment...
echo --------------------------------------------
python -m venv venv

echo.
echo --------------------------------------------
echo [2/5] Activating virtual environment...
echo --------------------------------------------
call venv\Scripts\activate

echo.
echo --------------------------------------------
echo [3/5] Installing Python dependencies...
echo --------------------------------------------
pip install --upgrade pip
pip install -r req.txt

echo.
echo --------------------------------------------
echo [4/5] Checking Ollama installation...
echo --------------------------------------------
where ollama >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ❌ Ollama is not installed. Please install from https://ollama.com/download
    pause
    exit /b
) else (
    echo ✅ Ollama found!
)

echo.
echo --------------------------------------------
echo [5/5] Pulling mistral:7b-instruct model...
echo --------------------------------------------
ollama list | findstr /i "mistral:7b-instruct" >nul
if %errorlevel% neq 0 (
    echo Pulling model...
    ollama pull mistral:7b-instruct
) else (
    echo ✅ Model mistral:7b-instruct already available!
)

echo.
echo ✅ Setup completed successfully.
pause
