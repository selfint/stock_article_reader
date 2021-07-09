import os

from dotenv import load_dotenv

from stock_article_reader.reader import Reader

load_dotenv()
API_KEY = os.environ.get("apikey")


def test_reader_constructor():
    r = Reader(API_KEY)

    assert isinstance(r, Reader)


def test_reader_returns_at_least_one_article():
    r = Reader(API_KEY)

    article_urls = r._get_articles("aapl")
    total_articles = len(article_urls)

    assert total_articles > 0
