from abc import ABC, abstractmethod
from pathlib import Path


class FileHandler(ABC):
    @abstractmethod
    def can_handle(self, file_path: Path) -> bool:  ## How robust is this?
        pass

    @abstractmethod
    def extract_text(
        self, file_path: Path
    ) -> str:  ## How robust is this? How do we know the text is extracted correctly?
        pass
