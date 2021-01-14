import requests
import json
import os
if os.path.exists("env.py"):
    import env

signin_data = {"password": os.environ.get("password"),"userName": "robknowles"}
signin_request = requests.post("https://api.lvs.linius.com/v2/iam/auth/signin", json=signin_data)
print(signin_request.content)

