from src.lib.file_handler import FileHandler as fh
from pdf2image import convert_from_path
from pathlib import Path
import pytesseract
import pypdf


class PDFHandler(fh):
    def can_handle(self, file_path: Path) -> bool:
        return file_path.suffix.lower() == ".pdf"

    def is_text_based(self, file_path: Path) -> bool:
        try:
            with open(file_path, "rb") as f:
                reader = pypdf.PdfReader(f)
                return any(page.extract_text() for page in reader.pages)
        except:
            return False

    def extract_text(self, file_path: Path) -> str:
        if self.is_text_based(file_path):
            with open(file_path, "rb") as f:
                reader = pypdf.PdfReader(f)
                return "\n".join(page.extract_text() or "" for page in reader.pages)
        else:
            pages = convert_from_path(file_path)
            return "\n".join(pytesseract.image_to_string(p) for p in pages)
