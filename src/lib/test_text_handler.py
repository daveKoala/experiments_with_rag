from lib.txt_handler import TxtHandler
from pathlib import Path
import pytest


@pytest.fixture
def txt_handler():
    return TxtHandler()


def test_txt_handler_can_handle_txt_file(txt_handler):
    assert txt_handler.can_handle(Path("document.txt")) is True


def test_txt_handler_cannot_handle_pdf_file(txt_handler):
    assert txt_handler.can_handle(Path("document.pdf")) is False
