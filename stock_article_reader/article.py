import datetime
from typing import NamedTuple


class Article(NamedTuple):
    ticker: str
    published_date: datetime.datetime
    title: str
    image_url: str
    site_name: str
    snippet: str
    url: str
    sentiment: float
    summary: str
