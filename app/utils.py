import openai
from sentence_transformers import SentenceTransformer
from app.database import save_embeddings, get_relevant_docs
from sqlalchemy.ext.asyncio import AsyncSession
from app.shared import generate_embeddings

# Initialize the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
openai.api_key = 'test_key'

def store_embeddings_in_db(filename: str, embeddings: list, db: AsyncSession):
    save_embeddings(filename, embeddings, db)

async def retrieve_documents(query: str, db: AsyncSession):
    query_embedding = generate_embeddings(query)
    relevant_docs = await get_relevant_docs(query_embedding, db)
    return relevant_docs

# Function to generate the answer based on the context and query
def generate_answer(query: str, documents: list):
    # Combine all document contents into a single context string
    context = " ".join([doc["content"] for doc in documents])
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Answer the following question using the context: {context}\n\n{query}"}
        ],
        max_tokens=200
    )
    return response.choices[0]["message"]["content"].strip()


