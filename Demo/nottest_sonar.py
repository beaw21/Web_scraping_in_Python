import requests
s = requests.Session()
s.auth = ('admin','admin21')
auth = s.post('http://localhost:9000')
response = s.get('http://localhost:9000/api/projects/search')
print(response.json())