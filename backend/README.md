# Finale backend

FastAPI app served with the static frontend export. Run locally:

```bash
uv sync --group dev
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Set `OPENAI_API_KEY` in the environment or `.env`.
