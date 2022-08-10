from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import __version__

# check version
# print(sys.path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# print(__version__)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
driver.get("https://github.com/apache/hive")



driver.find_element(By.ID, "pull-requests-tab").click()
time.sleep(5)
print("ok")

driver.find_element(By.CLASS_NAME, "btn-link").click()
time.sleep(5)
print("ok")
