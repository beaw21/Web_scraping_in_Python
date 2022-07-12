import requests
from bs4 import BeautifulSoup
url = "https://github.com/apache/hive/pulls?q=is%3Apr+is%3Aclosed"
req = requests.get(url)
print(req)

req.encoding = "utf-8"
soup =BeautifulSoup(req.text, 'html.parser')
print(soup.prettify())

c = soup.find_all('a')
print(c)