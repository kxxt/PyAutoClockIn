Remove-Item -r dist
pyinstaller clockin.spec
Copy-Item chromedriver.exe dist\
Copy-Item README.MD dist\README.MD
Copy-Item settings.json .\dist\
Set-Location dist
zip -9 -q ..\release-nochrome.zip .\*
Set-Location ..