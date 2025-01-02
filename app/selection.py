from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import select_documents
from app.qna import get_db

router = APIRouter()

@router.get("/select")
async def select_documents_for_qna(
    selected_ids: list[int] = Query(...), 
    db: AsyncSession = Depends(get_db)
):
    print("Selected IDs:", selected_ids)
    try:
        selected = await select_documents(selected_ids, db)
        return {"selected_documents": selected}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
