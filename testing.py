import requests
import json
import os
from proxy import Proxy
if os.path.exists("env.py"):
    import env

robs_proxy = Proxy("robknowles", os.environ.get("password"))
print(robs_proxy.token)