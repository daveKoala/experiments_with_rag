def AppendToTextFile(filename: str, text: str, mode: str = "a") -> None:
    with open(filename, mode, encoding="utf-8") as f:
        f.write(text + "\n")
