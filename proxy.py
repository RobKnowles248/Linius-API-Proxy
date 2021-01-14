import requests
import json
import os


class Proxy():

    def __init__(self, userName, password, API_key):
        """
        Method that creates a class variable of token which gives the oAuth token
        """
        signin_data = {"password": password, "userName": userName}
        try:
            signin_request = requests.post("https://api.lvs.linius.com/v3/iam/auth/signin", json=signin_data)
            self.token = signin_request.json()["token"]
        except KeyError:
            raise ValueError("Username or password incorrect!")
        self.API_key = API_key
        self.headers = {"authorization": "Bearer " + self.token, "x-api-key": self.API_key}


    def validateToken(self):
        """
        Method that validates an oAuth token for the Linius API
        """
        headers = {"authorization": "Bearer " + self.token}
        validate_request = requests.get("https://api.lvs.linius.com/v3/iam/auth/token/validate", headers=headers)
        if validate_request.status_code == 200:
            return "Valid"
        elif validate_request.status_code == 401:
            return "Invalid"


    def discover(self, sourceUrl, endDate=None, mediaFormat=None, name=None, startDate=None, tags=None, thumbnailUrl=None):
        """
        Method that will discover and process Audio/Video assets and save relevant info in the Linius platform

        :sourceUrl: string, source URL of the media asset
        :endDate: Date-time, End date of activation, can be absent
        :format: String, source format, default: MP4
        :name: string, name for discovered asset, generated if absent
        :startDate: Date-time, Start date of activation, can be absent
        :tags: list, Asset tags, Set of 0 or more tags each as individual strings
        :thumbnailUrl: URL of video thumbnail

        :returns: response object for the API call
        """
        request_body = {
            "sourceUrl": sourceUrl,

        }
        optional_args = {"endDate": endDate, "media": mediaFormat, "name": name, "tags": tags, "thumbnailUrl": thumbnailUrl}
        for key, val in optional_args.items():
            if val:
                request_body[key] = val
        discover_request = requests.post("https://api.lvs.linius.com/v3/discover", headers=self.headers, json=request_body)
        return discover_request.json()


    def enrich_assets(self, assetId, workflowId=2):
        """
        Method that will enrich a discovered asset

        :assetId: String, Valid ID of Discovered Asset
        :workflowId: Int32, Indicates the specific data provider and clip metadata schema. Standard workflow ID is 2.
        """
        request_body = {
            "assetId": assetId,
            "workflowId": workflowId
        }
        enrich_assets_request = requests.post("https://api.lvs.linius.com/v3/enrich/assets", headers=self.headers, json=request_body)
        return enrich_assets_request.json()


    def enrich_jobs(self, assetIds):
        """
        Method that allows you to get the statuses of multiple Enrichment jobs by providing multiple assetIds.

        :id: Array, Multiple assetIds of discovered Assets
        """
        enrich_jobs_request = requests.get("https://api.lvs.linius.com/v3/enrich/jobs", params={"id": assetIds}, headers=self.headers)
        return enrich_jobs_request.json()


    def search(self, query, page=None, pageSize=None, sortMode=None, sortDesc=None, addHighlights=None):
        """
        Method that searches for videoclip objects within one or multiple discovered video assets
        """
        request_body = {
            "query": query
        }
        optional_args = {"page": page, "pageSize": pageSize, "sortMode": sortMode, "sortDesc": sortDesc, "addHighlights": addHighlights}
        for key, val in optional_args.items():
            if val:
                request_body[key] = val

        search_request = requests.get("https://api.lvs.linius.com/v3/search", params=request_body, headers=self.headers)
        return search_request.json()