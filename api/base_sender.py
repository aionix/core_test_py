import requests
# class BaseSender:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password
#
#     global base_url
#
BASE_URL = "http://104.248.133.198:8080/login"

def login():
    creds = {"username":"admin","password":"admin"}
    response = requests.post(BASE_URL, json=creds)
    return response.json()['accessToken']
