from src.lib.file_handler import FileHandler as fh
from pathlib import Path


# This is a simple text file handler that reads the content of a .txt file
# and returns it as a string.
class TxtHandler(fh):
    def can_handle(self, file_path: Path) -> bool:
        return file_path.suffix.lower() == ".txt"

    def extract_text(self, file_path: Path) -> str:
        return file_path.read_text(encoding="utf-8")
