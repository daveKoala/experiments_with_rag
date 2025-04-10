# I'm Batman

This project is an internal tool designed to help teams search and retrieve information from our growing collection of documents — thousands of `.txt`, .`pdf`, and other file types spread across our systems.

Initially, I explored chunking, tokenization, and vector-based search to enable semantic querying. While promising in theory, the results were patchy in practice — inconsistent, sometimes irrelevant, and often complex to debug.

That led to a rethink.

_Maybe the problem isn’t "how do we use the latest AI tools?"_
_Maybe it’s simply: how do we help people find useful information quickly and reliably?_

We’re now starting with a **keyword-based search**, which:

Returns whole documents, text excerpts, or references

Supports synonyms and query expansion

Can later be enhanced with vector or hybrid search if needed

The goal is to build something **useful first**, then smarter.

This is an evolving project, and as we there are some known unknowns and many unknown unknowns

## Set up virtual environment

### Create new virtual environment

From the root of the project

```
python3 -m venv .venv
```

To activate it

```
source .venv/bin/activate
```

To deactivate

```
deactivate
```

## Questions, Problems, etc

_Scanning password protected documents._ We can not just up a connection to a document repository and let it go wild trawling across multiple levels of files and directories. When it meets locked files it could return a reference to it for human intervention or flagged in some way.

_Scanned PDF's._ What i can see is there are two basic types of PDF. These are text or image. Scans of documents tend to be images, this adds additional potential errors.
