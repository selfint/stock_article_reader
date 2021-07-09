import os

from dotenv import load_dotenv

from stock_article_reader.reader import Reader

load_dotenv()
API_KEY = os.environ.get("apikey")

# create reader and get articles once
# since fmp api bills by call
r = Reader(API_KEY)
articles = r._get_articles(
    "aapl",
    limit=10,
    ignore_sources=["zacks investment research", "pymnts", "investorplace"],
)


def test_reader_constructor():
    assert isinstance(r, Reader)


def test_reader_returns_at_least_one_article():
    total_articles = len(articles)

    assert total_articles > 0


def test_get_article_summaries_and_sentiment():
    for article in articles:
        assert isinstance(article.summary, str)
        assert len(article.summary) > 0
        assert article.sentiment is not None
