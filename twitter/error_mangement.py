from requests import Response


class TwitterError(Exception):
    def __init__(self, status_message, status_code, url, response=None):
        self.status_message = status_message
        self.status_code = status_code
        self.url = url
        self.response = response
        super().__init__(f"Error {status_code}: {status_message} for url {url}.")


class RateLimitReachedError(TwitterError):
    def __init__(self, url, response=None):
        self.response = response
        super().__init__("Rate limit exceeded.", 429, url, response=response)


def parse_error(r: Response):
    if 400 <= r.status_code < 600 and r.status_code != 429:
        error_message = r.text
        if r.json():
            error_message = r.json()
            if "errors" in error_message:
                errors = error_message["errors"]
                if len(errors) > 0:
                    error_message = ", ".join(
                        ["'" + error["message"] + "'" for error in errors]
                    )

        raise TwitterError(error_message, r.status_code, r.url, response=r)
    elif r.status_code == 429:
        raise RateLimitReachedError(r.url, response=r)

    r.raise_for_status()
    return r.json()
