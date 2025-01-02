from pydantic import BaseModel
from fastapi import Depends, APIRouter, HTTPException
from app.database import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils import retrieve_documents, generate_answer

router = APIRouter()
print("Q&A router created")

class QueryRequest(BaseModel):
    query: str

# Dependency to get the database session
async def get_db():
    print("Creating database session")
    db = SessionLocal()
    print("Database session created")
    try:
        print(db)
        yield db
    except Exception as e:
        print("Error creating database session")
        raise e
    finally:
        print("Closing database session")
        pass  # Let FastAPI handle session lifecycle

@router.post("/qna")
async def ask_question(request: QueryRequest, db: AsyncSession = Depends(get_db)):
    print("Received question:", request.query)
    try:
        print("Query:", request.query)
        relevant_docs = await retrieve_documents(request.query, db)
        print("Relevant documents:", relevant_docs)
        answer = generate_answer(request.query, relevant_docs)
        return {"query": request.query, "answer": answer, "relevant_documents": relevant_docs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))