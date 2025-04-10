from src.lib.text_file import TextFile


def CreateMetaData(doc: TextFile, separator: bool = True) -> str:
    metaString = ""
    metaString = metaString + f"__META__FILE__TYPE: {doc.suffix.lower()}\n"
    metaString = metaString + f"__META__FILE__NAME: {doc.filename}\n"
    metaString = metaString + f"__META__FILE__SOURCE: {doc.source}\n"
    metaString = metaString + f"__META__FILE__SIZE: {doc.size}\n"
    metaString = metaString + f"__META__FILE__DATE: {doc.date}\n"
    if separator:
        metaString = metaString + "\n" + "=" * 80 + "\n\n"  ## Document separator
    else:
        metaString = metaString + "\n"

    return metaString
