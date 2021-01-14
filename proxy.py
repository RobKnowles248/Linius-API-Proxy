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

print(signin("robknowles", os.environ.get("password")))
