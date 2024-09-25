import requests

endpoint = 'http://127.0.0.1:8000/api/v1/main/services/steps/'
print(requests.get(endpoint, headers={'accept-language': 'uz'}).json())
