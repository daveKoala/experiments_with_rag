from lib.pdf_handler import PDFHandler

from pathlib import Path
import pytest


@pytest.fixture
def pdf_handler():
    return PDFHandler()


def test_pdf_handler_can_handle_pdf_file(pdf_handler):
    assert pdf_handler.can_handle(Path("document.pdf")) is True


def test_pdf_handler_cannot_handle_pdf_file(pdf_handler):
    assert pdf_handler.can_handle(Path("document.txt")) is False
