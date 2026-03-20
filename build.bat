@echo off
cd /d "%~dp0"
jupyter-book build edap
echo.
echo Open in browser: edap\_build\html\index.html
pause
