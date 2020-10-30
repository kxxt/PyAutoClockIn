# 请将Chrom(ium/e) 安装放置在 chrome-win 文件夹下
Remove-Item -r dist
pyinstaller clockin.spec
Copy-Item chromedriver.exe dist\
Copy-Item README.MD dist\README.MD
Copy-Item standardalone.json .\dist\
Copy-Item -Recurse .\chrome-win .\dist\chrome-win
Set-Location dist
zip -9 -q release.zip .\* .\*\*
Set-Location ..