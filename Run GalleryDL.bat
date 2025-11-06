@echo off
cd /d "%~dp0"
rem Use 'py -3' to ensure this runs with Python 3, since main.py uses f-strings
py -3 main.py
pause