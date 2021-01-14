import requests
import json
import os
if os.path.exists("env.py"):
    import env

def signin(userName, password):
    """
    Function that signs into the Linius API and returns an oAuth code.
    """
    signin_data = {"password": password, "userName": userName}
    signin_request = requests.post("https://api.lvs.linius.com/v2/iam/auth/signin", json=signin_data)
    return signin_request.json()["token"]

my_token = signin("robknowles", os.environ.get("password"))

def validateToken(token):
    """
    Function that validates an oAuth token for the Linius API
    """
    headers = {"authorization": "Bearer " + token}
    validate_request = requests.get("https://api.lvs.linius.com/v2/iam/auth/token/validate", headers=headers)
    if validate_request.status_code == 200:
        return "Valid"
    elif validate_request.status_code == 401:
        return "Invalid"

print(validateToken(my_token))