from stock_article_reader.reader import Reader


def test_reader_constructor():
    r = Reader()
    assert isinstance(r, Reader)
