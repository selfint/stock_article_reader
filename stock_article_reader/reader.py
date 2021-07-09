from typing import List

import fmpsdk

from stock_article_reader.article import Article

FMP = "https://financialmodelingprep.com/api/"


class Reader:
    def __init__(self, api_key: str):
        self._api_key = api_key
        # Company Valuation Methods

    def _get_articles(self, ticker: str, limit: int = 10) -> List[Article]:
        """Get list of URLs of articles relevant to ticker"""

        article_dicts = fmpsdk.stock_news(
            apikey=self._api_key, tickers=ticker.upper().strip(), limit=limit
        )

        articles = []
        for article_dict in article_dicts:
            article = Article(
                ticker=article_dict["symbol"],
                published_date=article_dict["publishedDate"],
                title=article_dict["title"],
                image_url=article_dict["image"],
                site_name=article_dict["site"],
                snippet=article_dict["text"],
                url=article_dict["url"],
            )
            articles.append(article)

        return articles
