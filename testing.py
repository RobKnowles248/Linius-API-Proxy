import requests
import json
import os
from proxy import Proxy
if os.path.exists("env.py"):
    import env

# Call the proxy
test_proxy = Proxy("robknowles", os.environ.get("password"), os.environ.get("API_key"), os.environ.get("API_url"))

# Testing the init method
test_token = test_proxy.token
print(f"Token: {test_token}")

test_headers = test_proxy.headers
print("")
print(f"Headers: \n{test_headers}")

# Testing discover method
print("")
test_discover = test_proxy.discover("https://linius-lvs.s3.amazonaws.com/demo/tears-of-steel.mp4")
print(f"Discover method output: \n{test_discover}")

# Testing enrich assets method
print("")
test_enrich_assets = test_proxy.enrich_assets("624311", 2)
print(f"Enrich assets method output: \n{test_enrich_assets}")

# Testing enrich jobs method
print("")
test_enrich_jobs = test_proxy.enrich_jobs(["624311"])
print(f"Enrich jobs method output: \n{test_enrich_jobs}")

# Testing search method
print("")
test_search = test_proxy.search("tears")
print(f"Search method output: \n{test_search}")