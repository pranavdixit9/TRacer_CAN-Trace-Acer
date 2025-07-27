@echo off
REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Navigate to the scripts directory
cd scripts

REM Run app.py using streamlit module from the venv's Python
python -m streamlit run app.py

pause
