import os
from pathlib import Path
import time
from appscript import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC1
from selenium.webdriver.common.by import By

# download from https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome('/{}/Downloads/chromedriver'.format(Path.home())) # change as per your location
driver.get("https://in.tradingview.com/chart/?symbol=WK")

driver.maximize_window()

ActionChains(driver).key_down(Keys.ALT).send_keys('s').perform()
wait_time = 25 # a very long wait time
element = WebDriverWait(driver, wait_time).until(EC1.element_to_be_clickable((By.LINK_TEXT, 'Save image')))
element.click()
time.sleep(3)
driver.close()

# selenium saves the file here
fname = '{}/Downloads/download.png'.format(Path.home())

# set screensaver
se = app('System Events')
desktops = se.desktops.display_name.get()
for d in desktops:
    desk = se.desktops[its.display_name == d]
    desk.picture.set(mactypes.File(fname))


# remove file
# os.remove(fname)
