import requests

# session = requests.Session()
# session.auth = ('admin', 'admin21')
# auth = session.post('http://localhost:9000')
# print("Response ::", auth)

url_api = 'http://localhost:9000'

params = {
    "scopes": "MAIN",
    "types": "CODE_SMELL",
    "languages": "java",
    "projects": "jspwiki-576bbb08533db274c09095812ae8a658c5983575",
    "resolved": "false",
    "ps": 500,
    "p": 1
}


def session(url, params):
    session = requests.Session()
    session.auth = ('admin', 'admin21')
    auth = session.post(url)
    return auth


URL = session(url_api, params=params)
print("Response ::", URL)
