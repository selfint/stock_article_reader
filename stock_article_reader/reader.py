import time
from typing import List, Optional

import fmpsdk
import newspaper
import nltk
from newspaper import Article as NewspaperArticle
from nltk.sentiment import SentimentIntensityAnalyzer

from stock_article_reader.article import Article

nltk.download("vader_lexicon")
nltk.download("punkt")


class Reader:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._analyzer = SentimentIntensityAnalyzer()

    def get_articles(
        self, ticker: str, limit: int = 10, ignore_sources: Optional[List[str]] = None
    ) -> List[Article]:
        """Get list of URLs of articles relevant to ticker"""

        article_dicts = fmpsdk.stock_news(
            apikey=self._api_key,
            tickers=ticker.upper().strip(),
            limit=limit,
        )

        articles = []
        for article_dict in article_dicts:
            if ignore_sources is not None:
                if article_dict["site"].lower().strip() in ignore_sources:
                    continue

            if "youtube" in article_dict["url"].lower():
                continue

            paper = NewspaperArticle(article_dict["url"])
            try:
                paper.download()
                paper.parse()
            except newspaper.article.ArticleException:
                continue
            paper.nlp()
            summary = paper.summary
            sentiment = self._analyzer.polarity_scores(paper.text)["compound"]

            article = Article(
                ticker=article_dict["symbol"],
                published_date=article_dict["publishedDate"],
                title=article_dict["title"],
                image_url=article_dict["image"],
                site_name=article_dict["site"],
                snippet=article_dict["text"],
                url=article_dict["url"],
                summary=summary,
                sentiment=sentiment,
            )
            articles.append(article)

            time.sleep(0.2)

        return articles
