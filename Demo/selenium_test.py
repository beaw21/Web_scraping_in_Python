from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://github.com/apache/hive/pulls?q=is%3Apr+is%3Aclosed")

elements = driver.find_element(by="d-block d-md-none position-absolute top-0 bottom-0 left-0 right-0")

print(elements)