from typing import Optional
import os
from pathlib import Path


class Settings:
    def __init__(self) -> None:
        self.BASE_PATH: Path = Path(__file__).resolve().parent.parent
        self.DATA_DIR: Path = self.BASE_PATH / "data/raw"
        self.API_KEY: Optional[str] = os.getenv("MY_API_KEY")
        self.PROCESSED_FILE: Path = self.BASE_PATH / "data/cleaned/cleaned_text.txt"
        self.CHUNKED_FILE: Path = self.BASE_PATH / "chunked_data.txt"
        self.VECTOR_STORE: Path = self.BASE_PATH / "vector_index_local.parquet"
        self.JSONL_FILE: Path = self.BASE_PATH / "data/cleaned/cleaned_text.jsonl"
        self.CHUNK_SIZE: int = 512
        self.CHUNK_OVERLAP: int = 50
        self.DEBUG: bool = False
        self.SENTENCE_TRANSFORMER_MODEL: str = (
            "all-MiniLM-L6-v2"  ##"sentence-transformers/all-MiniLM-L6-v2"
        )
        self.SENTENCE_TRANSFORMER_CHUNK_SIZE: int = 500
        self.SENTENCE_TRANSFORMER_OVERLAP_SIZE: int = 50

    def __repr__(self) -> str:
        config_lines = []
        for key, value in self.__dict__.items():
            # Mask any field that looks like a secret/key/token
            masked = "***" if "key" in key.lower() or "token" in key.lower() else value
            config_lines.append(f"  {key}={masked}")
        return "Settings(\n" + "\n".join(config_lines) + "\n)"


settings = Settings()
