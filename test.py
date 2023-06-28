from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--incognito') # private mode
# width of window size should be larger than certain value for access time_btn
options.add_argument('--window-size=1600,1080')
options.add_experimental_option("excludeSwitches", ['enable-logging']) # disable unused messages

