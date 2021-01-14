import requests
import json
import os


class Proxy():

    def __init__(self, userName, password):
        """
        Method that creates a class variable of token which gives the oAuth token
        """
        signin_data = {"password": password, "userName": userName}
        signin_request = requests.post("https://api.lvs.linius.com/v2/iam/auth/signin", json=signin_data)
        self.token = signin_request.json()["token"]
        

    def validateToken(self):
        """
        Function that validates an oAuth token for the Linius API
        """
        headers = {"authorization": "Bearer " + self.token}
        validate_request = requests.get("https://api.lvs.linius.com/v2/iam/auth/token/validate", headers=headers)
        if validate_request.status_code == 200:
            return "Valid"
        elif validate_request.status_code == 401:
            return "Invalid"