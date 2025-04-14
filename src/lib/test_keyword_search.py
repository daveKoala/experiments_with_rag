from lib.keyword_search import keyword_search as kws


def test_kws_returns_a_string():
    """
    Test if the keyword_search function returns a string.
    """
    result = kws("What is the capital of France?")
    assert isinstance(result, str), "The result should be a string."


def test_keyword_search_basic_cleaning():
    result = kws("What is the capital of France?")
    assert result == "What is the capital of France", f"Unexpected result: {result}"
