from lib.clean_text import CleanText


def test_removes_extra_whitespace():
    raw = "This    has     too many   spaces.\n\nAnd line breaks."
    result = CleanText(raw)
    assert result == "This has too many spaces. And line breaks."


def test_removes_page_numbers_case_insensitive():
    raw = "Some text before Page 1 and some after. also page 12 here."
    result = CleanText(raw)
    assert result == "Some text before and some after. also here."


def test_removes_non_printable_chars():
    raw = "Hello\u200b\u0007World!"  # Zero-width space + bell
    result = CleanText(raw)
    assert result == "HelloWorld!"


def test_strips_start_and_end_whitespace():
    raw = "     \n\n  Trim me please!   \t\t  "
    result = CleanText(raw)
    assert result == "Trim me please!"


def test_remives_html_tags():
    raw = "<p>This is a <b>test</b> string.</p>"
    result = CleanText(raw)
    assert result == "This is a test string."
