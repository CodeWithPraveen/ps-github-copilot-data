# Globomantics Checkout Service

Demo codebase for the Pluralsight course **GH-300: Understanding GitHub Copilot Data and Architecture**.

A minimal slice of the Globomantics e-commerce backend. Intentionally small — each demo touches one or two files only.

## Stack

- Python 3.11
- pytest for tests
- Dataclasses for models (FastAPI/SQLAlchemy/Pydantic mentioned in `.github/copilot-instructions.md` to give Copilot stack context for the RTCF demo)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
