import json
from src.lib.text_file import TextFile


def append_jsonl_entry(doc: TextFile, cleaned: str, output_file: str) -> None:
    # Build a dictionary for the JSON entry
    json_entry = {
        "date": doc.date,
        "source": doc.source,
        "filename": doc.filename,
        "suffix": doc.suffix,
        "size": doc.size,
        "content": cleaned,  # or metaData + cleaned if you want full context
    }

    with open(output_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(json_entry) + "\n")
