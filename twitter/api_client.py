from requests import Session
from requests_oauthlib import OAuth1

from twitter.error_mangement import parse_error
from twitter.paths import PathOperation
from typing import Union


class ApiClient:
    request_session = None

    def __init__(self, basic_path="https://api.twitter.com", api_version="1.1"):
        self.basic_path = basic_path
        self.api_version = api_version

    @property
    def session(self):
        if not self.request_session:
            self.request_session = Session()
        return self.request_session

    @property
    def api_path(self):
        return self.basic_path + "/" + self.api_version

    def parse_path(self, path: Union[PathOperation, str]):
        if type(path) == str:
            return path
        p = self.basic_path
        if path.version_requirement:
            p += "/" + self.api_version
        p += "/" + "/".join(path.raw_path)
        return p

    def request(self, method, path, **kwargs):
        return parse_error(
            self.session.request(method, self.parse_path(path), **kwargs)
        )


class TwitterRawApi:
    def __init__(
        self,
        consumer_key,
        consumer_private,
        access_token_key,
        access_token_secret,
        basic_path="https://api.twitter.com",
        api_version="1.1",
    ):

        self.auth = OAuth1(
            consumer_key, consumer_private, access_token_key, access_token_secret
        )

        self.client = ApiClient(basic_path=basic_path, api_version=api_version)

    def full_authenticated_request(self, method, path, **kwargs):
        if "params" in kwargs:
            new_params = {}
            for k, v in kwargs["params"].items():
                if not (v is None or v == "" or v == []):
                    new_params[k] = v
            kwargs["params"] = new_params
        return self.client.request(method, path, auth=self.auth, **kwargs)
