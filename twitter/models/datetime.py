from datetime import datetime

from twitter.models import TranslatedTwitterObject


class TwitterDatetime(TranslatedTwitterObject):
    def __init__(self, raw: str):
        self.raw = raw

    @property
    def datetime(self) -> datetime:
        return datetime.strptime(self.raw, "%a %b %d %H:%M:%S +0000 %Y")
