@echo off

cd ..

REM Activate the virtual environment
call env\Scripts\activate.bat

REM Run the script
python main.py

@REM REM Deactivate the virtual environment
@REM deactivate