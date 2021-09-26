import json
import requests

def msgraph_get(http_headers, url, out_file_name):
    data = requests.get(url, headers=http_headers, stream=False)
    with open(out_file_name, "w", encoding="utf-8") as out_file:
        out_file.write(json.dumps(data.json()))
    print(f"Called: {url}")

def msgraph_post(http_headers, body_data, url, out_file_name):
    response = requests.post(url, headers=http_headers, data=json.dumps(body_data), stream=False)
    with open(out_file_name, "w", encoding="utf-8") as out_file:
            out_file.write(json.dumps(response.json()))
    print(f"{response.status_code} Called: {url}")

with open("app-secrets.json", "r", encoding="utf-8") as app_settings_file:
    app_settings = json.load(app_settings_file)

with open("access-token.json", "r", encoding="utf-8") as access_token_file:
    access_token = json.load(access_token_file)

http_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token['access_token']}"
}

from mstodo import MsTodoApi

api = MsTodoApi()
api.get_task_list()