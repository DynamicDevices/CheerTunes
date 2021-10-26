@echo off

:: ENTER THE DETAILS HERE FROM THE WEB APP YOU CREATE - SEE README.md FOR DETAILS

SET SPOTIPY_CLIENT_ID=
SET SPOTIPY_CLIENT_SECRET=
SET SPOTIPY_REDIRECT_URI=http://127.0.0.1/dummy

:: Run the Python script (needs Python3!)

python cheerlights_spotify.py
