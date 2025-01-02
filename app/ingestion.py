from fastapi import APIRouter, UploadFile, HTTPException, Depends
from app.utils import generate_embeddings, store_embeddings_in_db
from app.qna import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/ingest")
async def ingest_document(file: UploadFile, db: AsyncSession = Depends(get_db)):
    try:
        content = await file.read()
        embeddings = generate_embeddings(content.decode("utf-8"))
        store_embeddings_in_db(file.filename, embeddings, db)
        return {"message": "Document ingested successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
