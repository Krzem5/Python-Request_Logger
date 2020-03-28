@echo off
cls
start /min cmd /c "ngrok http 8000"
start /max cmd /c "python index.py"