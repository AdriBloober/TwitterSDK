from typing import List

from twitter.models import TwitterModel


class TwitterBoundingBox(TwitterModel):
    coordinates: List[List[List[float]]]
    type: str


class TwitterPlaces(TwitterModel):
    id: str
    url: str
    place_type: str
    name: str
    full_name: str
    country_code: str
    country: str
    bounding_box: TwitterBoundingBox


class TwitterCoordinates(TwitterModel):
    coordinates: List[float]
    type: str
