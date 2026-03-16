import json

import requests

api_endPoint = "https://api.openapi.com/v1/completions"
api_key = "sk-7x9g2IBmjbAqgT15yhCqT3B1bkFJPYWe1Ma88Q0cmmDEDtn6"

request_headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

request_data = {
    'model':'text-davinci-003',
    'promt':'Write python script for hello world',
    'max_tokens':100,
    'temperature':0.5
}

responce = requests.post(api_endPoint, data=json.dumps(request_data), headers=request_headers)
print(responce.text)