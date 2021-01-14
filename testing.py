import requests
import json
import os
from proxy import Proxy
if os.path.exists("env.py"):
    import env

# Call the proxy
robs_proxy = Proxy("robknowles", os.environ.get("password"), os.environ.get("API_key"))

# Testing the init method
#print(robs_proxy.token)
#print(robs_proxy.headers)

# Testing discover method
print(robs_proxy.discover(
    "Tears of Steel",
    "https://linius-lvs.s3.amazonaws.com/demo/tears-of-steel.mp4",
    ["Tears of Steel", "Demo5"],
    "http://www.gstatic.com/tv/thumb/movieposters/10875273/p10875273_p_v8_ac.jpg",
    False))