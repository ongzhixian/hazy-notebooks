""" Python app to complete the device code flow after user has done authentication.
    This module acts in tandem with fill_device_code_flow.py
"""

import json
import msal

with open("app-secrets.json", "r", encoding="utf-8") as app_settings_file:
    app_settings = json.load(app_settings_file)

# Create a preferably long-lived app instance which maintains a token cache.
app = msal.PublicClientApplication(
    app_settings["client_id"], 
    authority=app_settings["authority"]
)

with open("device-flow.json", "r", encoding="utf-8") as device_flow_file:
    flow = json.load(device_flow_file)

# By default 'acquire_token_by_device_flow' will poll if user has done authentication and block current thread.
# You can abort the polling loop at any time, by changing the value of the flow’s “expires_at” key to 0.
# And then keep calling acquire_token_by_device_flow(flow) in your own customized loop
# We do polling here assuming somehow that we will get the signal to read the access token.

access_token = app.acquire_token_by_device_flow(flow)  

print(access_token)

with open("access-token.json", "w", encoding="utf-8") as output_file:
    output_file.write(json.dumps(access_token))
