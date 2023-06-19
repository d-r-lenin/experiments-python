@echo off

cd ..

REM Create a virtual environment
python -m venv env

REM Activate the virtual environment
call env\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Deactivate the virtual environment
deactivate