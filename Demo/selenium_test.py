import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#check version
print(sys.path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://camt.cmu.ac.th")

