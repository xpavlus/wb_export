import os

import requests

from dotenv import load_dotenv

load_dotenv()

wb_token = os.getenv('WB_TOKEN')
mpstat_token = os.getenv('MPSTAT_TOKEN')


class APIRequest:
    __header = {}
    default_domain = "statistics-api.wildberries.ru"

    def __init__(self, domain=None, token=None):
        self.domain = domain or self.default_domain
        self.__token = token or wb_token
        self.__header["Authorization"] = self.__token

    def _get(self, path, param=None):
        if isinstance(path, str):
            if path.startswith("/api/v1/"):
                _api_path = path.replace("/api/v1/", "")
            else:
                _api_path = path
        else:
            raise ValueError(f"path should be a string, but it is {type(path)} instead")
        _response = requests.get(
            f"https://{self.domain}/api/v1/{_api_path}",
            headers=self.__header,
            params=param
        )
        if _response.status_code == 429:
            raise APITechBreak()
        return _response

    def get_json(self, path, param=None):
        _response = self._get(path, param)
        if _response.ok:
            return _response.json()
        else:
            return []


class APIRequestException(Exception):
    pass


class APITechBreak(APIRequestException):
    pass
