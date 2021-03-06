import selenium
from selenium import webdriver
from time import sleep
from datetime import datetime
import traceback
import platform
import json
# fallback values for settings.json
retrymax=2
printToConsole=True
silent=False
chromeBinaryPath=None
logSucceededRecord=True
# end fallback values
try:
    f=open("users.txt")
    log=open("log.txt","a")
    users=[x.strip() for x in f.readlines()]
except:
    log.close()
    exit(-1)
finally:
    f.close()
try:
    s=open("settings.json",encoding="utf8")
    settings=json.load(s)
    if "chrome" in settings:chromeBinaryPath=settings["chrome"]
    if "retrymax" in settings:retrymax= settings["retrymax"]
    if "silent" in settings:silent= settings["silent"]
    if "logsucceeded" in settings:logSucceededRecord= settings["logsucceeded"]
    if "print2con" in settings:printToConsole= settings["print2con"]
except:
    if printToConsole:print("settings.json not found or corrupted. Use default settings.")
finally:s.close()
def writelog(msg):
    log.write(msg)
    if printToConsole:print(msg)
if not users:
    writelog("Warning : no users in users.txt\nApp exiting.\n")
    sleep(5)
    exit(1)
options=webdriver.ChromeOptions()
mobileEmulation = {'deviceName': 'iPhone X'}
options.add_experimental_option('mobileEmulation', mobileEmulation)
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--hide-scrollbars')
options.add_argument('blink-settings=imagesEnabled=false')
options.add_argument('--disable-dev-shm-usage')
if silent:
    options.add_argument('--headless')
if chromeBinaryPath:
    options.binary_location= chromeBinaryPath
for user in users:
    for i in range(retrymax):
        try:
            driver=webdriver.Chrome( "chromedriver.exe" if platform.system()=="Windows" else"./chromedriver",chrome_options=options)
            driver.get("https://xsc-health.wh.sdu.edu.cn/mobile/index.html#/common/office/login")
            driver.maximize_window()
            driver.implicitly_wait(10)
            username=driver.find_element_by_name("username")
            password=driver.find_element_by_name("password")
            username.send_keys(user)
            password.send_keys(f"whsdu@{user}")
            driver.implicitly_wait(2)
            password.submit()
            driver.implicitly_wait(5)
            label=driver.find_element_by_class_name("grid-label")
            label.click()
            sleep(6)
            try:driver.execute_script("a=document.getElementsByClassName(\"weui-dialog__btn\")[0];a.click()")
            except : pass
            driver.implicitly_wait(5)
            driver.execute_script("a=document.getElementsByClassName(\"weui-btn_primary\")[0];a.click()")
        except Exception as e:
            writelog(f"===== Error Begin @ {datetime.now()} =====")
            writelog(f"Error occurred while clocking in ,try number = {i}, User = {user}.\nStack Trace:{traceback.format_exc()}\n")
            writelog(f"===== Error End  @ {datetime.now()}  =====")
        else:
            if logSucceededRecord:writelog(f"Success , user {user} , time {datetime.now()}\n")
            break
        finally:
            sleep(5)
            driver.quit()
            
log.close()