from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from app.models import Document, Embedding
from app.shared import generate_embeddings


DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost/python-backend"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def save_embeddings(filename: str, embeddings: list, db: AsyncSession):
    # Save a document with its embeddings
    async with db.begin():
        # Save the document
        document = Document(filename=filename)
        db.add(document)
        await db.flush()  # Generate document ID

        # Save embeddings
        db_embedding = Embedding(document_id=document.id, embedding=embeddings)
        db.add(db_embedding)

        await db.commit()

async def get_relevant_docs(query_embedding: list, db: AsyncSession):
    # Retrieve documents based on embedding similarity
    async with db.begin():
        documents = await db.execute(select(Document))
        documents = documents.scalars().all()

        # Placeholder for similarity logic: Replace with cosine similarity computation
        return [{"filename": doc.filename, "content": doc.content} for doc in documents]

async def select_documents(selected_ids: list, db: AsyncSession):
    # Retrieve documents based on selected IDs
    async with db.begin():
        result = await db.execute(select(Document).filter(Document.id.in_(selected_ids)))
        return result.scalars().all()
