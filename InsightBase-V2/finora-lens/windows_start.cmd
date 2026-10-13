@echo off
setlocal
set "IB_EDGE=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
if not exist "%IB_EDGE%" set "IB_EDGE=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
if not exist "%IB_EDGE%" (echo Microsoft Edge bulunamadi. & pause & exit /b 1)
start "" "%IB_EDGE%" --allow-file-access-from-files --user-data-dir="%TEMP%\InsightBase-Local" "%~dp0InsightBase.html"
endlocal
