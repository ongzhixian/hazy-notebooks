""" Python app to initialize the device code flow.
    This module acts in tandem with fill_device_code_flow.py
"""

import json
import msal

with open("app-secrets.json", "r", encoding="utf-8") as app_settings_file:
    app_settings = json.load(app_settings_file)

with open("access-token.json", "r", encoding="utf-8") as access_token_file:
    bearer_token = json.load(access_token_file)

# Create a preferably long-lived app instance which maintains a token cache.
app = msal.PublicClientApplication(
    app_settings["client_id"], 
    authority=app_settings["authority"]
)

refresh_token = bearer_token['refresh_token']
access_token = app.acquire_token_by_refresh_token(refresh_token, scopes=app_settings['scopes'])

# replace 
with open("access-token.json", "w", encoding="utf-8") as out_file:
    out_file.write(json.dumps(access_token))
