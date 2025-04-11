from lib.expand_question import expand_question_to_keywords as eqs


def test_expand_question_returns_a_dict():
    """
    Test that expand_question_to_keywords returns a properly shaped dictionary:
      - The result is a dictionary.
      - It contains expected keys (e.g., content words like "capital" and "france").
      - It does not include stopwords as keys (e.g., "what", "is", "the", "of").
      - Each value is a list of strings.
    """
    result = eqs("What is the capital of France?")
    print("Result:", result)

    # Ensure that a dictionary is returned
    assert isinstance(result, dict), "The result should be a dictionary."

    # Expected content words after stopword filtering
    expected_keys = {"capital", "france"}
    for key in expected_keys:
        assert key in result, f"Expected key '{key}' not found in the result."

    # Ensure stopwords have been removed
    stopword_keys = {"what", "is", "the", "of"}
    for key in stopword_keys:
        assert key not in result, f"Stopword '{key}' should have been filtered out."

    # Verify that each value is a list of strings
    for token, synonyms in result.items():
        assert isinstance(
            synonyms, list
        ), f"The synonyms for '{token}' should be a list."
        for syn in synonyms:
            assert isinstance(
                syn, str
            ), f"Each synonym for '{token}' should be a string."
