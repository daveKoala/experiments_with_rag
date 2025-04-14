import re  # Regular expressions


def keyword_search(question: str) -> str:
    """
    Formats the question and preps it for searching documents.

    Args:
        question (str): The string to search.

    Returns:
        string: Formatted and prepared string.
    """

    # question = question.lower() # This will loose context of proper names!!!!
    question = re.sub(r"[^\w\s]", "", question)  # Remove punctuation
    question = re.sub(r"\s+", " ", question).strip()  # Remove extra spaces
    return question
