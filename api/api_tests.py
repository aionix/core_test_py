import requests

##Login creds and api paths
login_json = {"username":"admin","password":"admin"}
base_url = "http://104.248.133.198:8080/login"
path_get_todo = "http://104.248.133.198:8080/todos"
###
auth_token = None

headers_fin = {"Authorization": "Bearer %s" % auth_token}
headers = {"Authorization": "Bearer %s" % auth_token}

def test_login():
    response = requests.post(base_url, json=login_json)
    code = response.status_code
    assert code == 200

def test_get_todos():
    #global auth_token

    response = requests.post(base_url, json=login_json)
    code = response.status_code
    assert code == 200

    auth_token = response.json()['accessToken']
    headers = {"Authorization": "Bearer %s" % auth_token}


    data = requests.get(path_get_todo, headers=headers)
    print(data.json()['1'])

test_get_todos()
