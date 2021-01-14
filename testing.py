import requests
import json
import os
from proxy import Proxy
if os.path.exists("env.py"):
    import env

robs_proxy = Proxy("robknowles", os.environ.get("password"), os.environ.get("API_key"))
print(robs_proxy.token)
print(robs_proxy.headers)