from bs4 import BeautifulSoup
import re  ## Regex for cleaning text

# So the idea is we can pass text extracted from a PDF to this function and it will clean it up
# and remove any unwanted characters, HTML tags, page numbers, etc.
# The function will return a cleaned string.
# The function will also remove any extra whitespace and line breaks.
# The function will also remove any non-printable characters.
# The function will also remove any page numbers.


## But there is so many different strings and content that this is only a starting point.
def clean_text(text: str) -> str:
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()  # Remove all HTML tags
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"Page \d+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text)
    text = "".join(c for c in text if c.isprintable())
    return text.strip()
