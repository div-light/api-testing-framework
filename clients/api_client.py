import requests
from utilities.logger import logger

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    
    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(
        url,
        params=params,
        headers=headers)

        return response

    def post(self, endpoint, data=None, json=None, params=None, headers=None):
        logger.info(f"POST {endpoint}")
        response = requests.post(
        self.base_url + endpoint,
        data=data,
        json=json,
        params=params,
        headers=headers)
        logger.info(f"Response status: {response.status_code}")
        return response

    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, data=data)
        return response
    
    def delete(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, data=data)
        return response




