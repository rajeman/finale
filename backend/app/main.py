from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routers import router as api_router

app = FastAPI(title="finale")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok"}


_static = Path.cwd() / "static"
if _static.is_dir():
    app.mount("/", StaticFiles(directory=str(_static), html=True), name="static")
