@echo off
cd /d "%~dp0"
jupyter-book clean edap
echo.
jupyter-book build edap
echo.
echo Open in browser: edap\_build\html\index.html
pause
