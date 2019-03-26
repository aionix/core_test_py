import json

import requests


class ToDoService():
    def __init__(self,  *args, **kwargs):
        self.base_url = "http://104.248.133.198:8080"

    def login_user(self):
        login_json = {"username":"admin","password":"admin"}
        response = requests.post(url=self.base_url + "/login", json=login_json)

        auth_token = response.json()['accessToken']
        headers = {"Authorization": "Bearer %s" % auth_token}
        return headers

    def get_todos(self, headers):
        return requests.get(url=self.base_url + "/todos", headers=headers)

    def add_todo(self, json_data, headers):
        #_json_data = json.dumps(json_data)
        return requests.post(url=self.base_url + "/todos", data=json_data, headers=headers)


