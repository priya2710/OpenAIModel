from fastapi import FastAPI
from app.ingestion import router as ingestion_router
from app.qna import router as qna_router
from app.selection import router as selection_router

app = FastAPI()

app.include_router(ingestion_router, prefix="/api/ingestion", tags=["Ingestion"])
app.include_router(qna_router, prefix="/api", tags=["Q&A"])
app.include_router(selection_router, prefix="/api/selection", tags=["Selection"])
