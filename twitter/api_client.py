from enum import Enum

from requests.auth import AuthBase, HTTPBasicAuth
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


class TwitterAuthType(Enum):
    OAuth1 = 0
    OAuth2_Bearer_Token = 1
    BasicAuth = 2


class TwitterAuth(AuthBase):
    def __init__(self, type_of_auth: TwitterAuthType, auth):
        self.type_of_auth = type_of_auth
        self.auth = auth

    def __call__(self, r):
        if self.type_of_auth == TwitterAuthType.OAuth1:
            if not type(self.auth) == OAuth1:
                raise ValueError(
                    "TwitterAuth.auth should be type requests_oauthlib.OAuth1!"
                )
            return self.auth(r)
        elif self.type_of_auth == TwitterAuthType.OAuth2_Bearer_Token:
            # self.auth is the bearer Token
            if not type(self.auth) == str:
                raise ValueError("TwitterAuth.auth should be type string!")
            r.headers["authorization"] = "Bearer " + str(self.auth)
            return r
        elif self.type_of_auth == TwitterAuthType.BasicAuth:
            if not type(self.auth) == tuple or not len(self.auth) == 2:
                raise ValueError(
                    "TwitterAuth.auth should be type tuple with (email_address, password)."
                )
            return HTTPBasicAuth(*self.auth)(r)
        else:
            raise ValueError(
                f"TwitterAuth.type_of_auth {self.type_of_auth} is unknown. Please use another auth method."
            )

    @staticmethod
    def get_oauth1_auth(
        oauth_consumer_key, oauth_consumer_secret, oauth_token, oauth_token_secret
    ):
        return TwitterAuth(
            TwitterAuthType.OAuth1,
            OAuth1(
                oauth_consumer_key,
                oauth_consumer_secret,
                oauth_token,
                oauth_token_secret,
            ),
        )

    @staticmethod
    def get_oauth2_bearer_token(bearer_token):
        return TwitterAuth(TwitterAuthType.OAuth2_Bearer_Token, bearer_token)

    @staticmethod
    def get_basic_authentication(email_address, password):
        return TwitterAuth(TwitterAuthType.BasicAuth, (email_address, password))


class TwitterRawApi:
    def __init__(
        self,
        auth: Union[TwitterAuth, AuthBase],
        basic_path="https://api.twitter.com",
        api_version="1.1",
    ):

        self.auth = auth

        self.client = ApiClient(basic_path=basic_path, api_version=api_version)

    def full_authenticated_request(self, method, path, **kwargs):
        if "params" in kwargs:
            new_params = {}
            for k, v in kwargs["params"].items():
                if not (v is None or v == "" or v == []):
                    new_params[k] = v
            kwargs["params"] = new_params
        return self.client.request(method, path, auth=self.auth, **kwargs)
