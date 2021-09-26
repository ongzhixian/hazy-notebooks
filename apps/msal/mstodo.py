import json
import requests

class MsTodoApi():
    def __init__(self):
        self.base_url = "https://graph.microsoft.com/v1.0/me/todo/lists"
        with open("access-token.json", "r", encoding="utf-8") as access_token_file:
            self.access_token = json.load(access_token_file)

    def get_http_headers(self):
        x = self.access_token
        import pdb
        pdb.set_trace()
        http_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token['access_token']}"
        }
        return http_headers

    def create_list(self, list_name):
        body_data = {
            "displayName": list_name
        }
        
        response = requests.post(
            self.base_url, 
            headers = self.get_http_headers(), 
            data = json.dumps(body_data), 
            stream = False)

        print(f"ok: {response.ok}, HTTP status code: {response.status_code}")

        if response.ok:
            response_json = response.json()
            print(f"displayName: {response_json['displayName']}")
            print(f"id: {response_json['id']}")
        else:
            print(response.text)
            print(response.json())
            
    def get_task_list(self):
        response = requests.get(
            self.base_url, 
            headers=self.get_http_headers(), 
            stream=False)

        print(f"ok: {response.ok}, HTTP status code: {response.status_code}")

        if response.ok:
            response_json = response.json()
            todo_list = response_json['value']
            for x in todo_list:
                displayName = x['displayName']
                id = x['id']
                print(f"Display name: {displayName}, Id: {id}")
        else:
            print(response.text)
            print(response.json())
