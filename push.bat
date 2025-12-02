@echo off
git add .
git commit -m "%~1"
git push origin main
echo ---------------------------
echo    UPLOAD SUCCESSFUL 🚀
echo ---------------------------
pause