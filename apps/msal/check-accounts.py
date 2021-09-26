""" Python app to initialize the device code flow.
    This module acts in tandem with fill_device_code_flow.py
"""

import json
import msal

with open("app-secrets.json", "r", encoding="utf-8") as app_settings_file:
    app_settings = json.load(app_settings_file)

# Create a preferably long-lived app instance which maintains a token cache.
app = msal.PublicClientApplication(
    app_settings["client_id"], 
    authority=app_settings["authority"],
)

# ZX: I think this is applicable only if we are caching tokens

accounts = app.get_accounts()
