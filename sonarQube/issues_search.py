import session_sonar

base_url = "http://localhost:9000/api/issues/search"
params = {
    "scopes": "MAIN",
    "types": "CODE_SMELL",
    "languages": "java",
    "projects": "jspwiki-576bbb08533db274c09095812ae8a658c5983575",
    "resolved": "false",
    "ps": 500,
}

get_api = session_sonar.session(base_url, params=params)