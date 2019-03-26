import requests




    # response = requests.post('http://localhost:8080/calculator/sqrt/1024')
    # print(response.content)

BASE_URL = "http://104.248.133.198:8080/login"

def calculator_api_sqrt():
        response = requests.post('http://localhost:8080/calculator/sqrt/1024')
        # if response.status_code !=300:
        #     print("wrong code: " + str(response.status_code))
        return response.json()['input']

def login():
    json = {"username":"admin","password":"admin"}
    response = requests.post(BASE_URL, json=json)
    print (response.json()['accessToken'])



print(calculator_api_sqrt())







