""" Python app to initialize the device code flow.
    This module acts in tandem with fill_device_code_flow.py
"""

import json
import msal
import requests

with open("app-secrets.json", "r", encoding="utf-8") as app_settings_file:
    app_settings = json.load(app_settings_file)

# Create a preferably long-lived app instance which maintains a token cache.
app = msal.PublicClientApplication(
    app_settings["client_id"], 
    authority=app_settings["authority"]
)

flow = app.initiate_device_flow(scopes=app_settings['scopes'])

if "user_code" not in flow:
    raise ValueError("Fail to create device flow. Err: %s" % json.dumps(flow, indent=4))

print(flow["message"])

with open("device-flow.json", "w", encoding="utf-8") as output_file:
    output_file.write(json.dumps(flow))
