from src.lib.file_handler import FileHandler as fh
from pathlib import Path


class DocumentLoader:
    def __init__(self):
        self.handlers: list[fh] = []

    def register_handler(self, handler: fh):
        self.handlers.append(handler)

    def extract_text(self, file_path: Path) -> str:
        for handler in self.handlers:
            if handler.can_handle(
                file_path
            ):  ## check if the handler can handle the file type
                ## if yes, call the extract_text method of the handler
                return handler.extract_text(file_path)
        raise ValueError(f"No handler for file type: {file_path.suffix}")
