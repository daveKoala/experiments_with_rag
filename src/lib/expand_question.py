from nltk.corpus import wordnet, stopwords
from nltk import download as nltk_download
import re
from src.config import settings

language = settings.LANGUAGE

# Try to load wordnet, download if missing
try:
    wordnet.ensure_loaded()
except LookupError:
    nltk_download("wordnet")
    wordnet.ensure_loaded()

# Ensure stopwords are loaded
try:
    stop_words = set(stopwords.words(language))
except LookupError:
    nltk_download("stopwords")

stop_words = set(stopwords.words(language))


# This is really just a first pass, there's a lot of room for improvement here.
# Note: This is a simple approach, we need to consider more sophisticated methods
# for synonym generation, such as using word embeddings or other NLP techniques.
def get_synonyms(word: str) -> list:
    """
    Retrieve up to 5 synonyms for the given word from WordNet,
    limiting to nouns and verbs and ignoring synonyms that look like proper names.
    """
    synonyms = set()
    for syn in wordnet.synsets(word):
        if syn.pos() not in ("n", "v"):  # Limit to nouns and verbs
            continue
        for lemma in syn.lemmas():
            name = lemma.name().replace("_", " ")
            # Skip if the synonym equals the word (ignoring case)
            if name.lower() == word.lower():
                continue
            # Prevent adding proper names or names with capital letters:
            if name != name.lower():
                continue
            synonyms.add(name)
    return list(synonyms)[:5]  # Limit to a maximum of 5 synonyms


def expand_question_to_keywords(question: str) -> dict:
    """
    Expand a question into a dictionary of keywords and their synonyms.

    Args:
        question (str): _description_

    Returns:
        dict: _description_
    """
    # Clean question first
    question = question.lower()
    question = re.sub(r"[^\w\s]", "", question)  # Or use the clean text method???
    tokens = question.strip().split()

    tokens = [token for token in tokens if token not in stop_words]

    # Remove duplicates
    tokens = list(dict.fromkeys(tokens))
    # Remove empty tokens
    tokens = [token for token in tokens if token]

    # Get synonyms for each token
    return {word: get_synonyms(word) for word in tokens}
