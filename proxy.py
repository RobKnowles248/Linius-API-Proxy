import requests
import json
import os


class Proxy():

    def __init__(self, userName, password, API_key):
        """
        Method that creates a class variable of token which gives the oAuth token
        """
        signin_data = {"password": password, "userName": userName}
        signin_request = requests.post("https://api.lvs.linius.com/v2/iam/auth/signin", json=signin_data)
        self.token = signin_request.json()["token"]
        self.API_key = API_key
        self.headers = {"authorization": "Bearer " + self.token, "x-api-key": self.API_key}


    def validateToken(self):
        """
        Method that validates an oAuth token for the Linius API
        """
        headers = {"authorization": "Bearer " + self.token}
        validate_request = requests.get("https://api.lvs.linius.com/v2/iam/auth/token/validate", headers=headers)
        if validate_request.status_code == 200:
            return "Valid"
        elif validate_request.status_code == 401:
            return "Invalid"


    def discover(self, name, sourceUrl, tags, thumbnailUrl, uploadSource):
        """
        Method that will discover and process Audio/Video assets and save relevant info in the Linius platform
        :name: string, name of the media asset
        :sourceUrl: string, source URL of the media asset
        :tags: list, list of tags for the media asset
        :uploadSource: boolean, decides if the media will be uploaded or just the headers will be stored
        """
        return 
