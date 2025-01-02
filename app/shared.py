from sentence_transformers import SentenceTransformer

# Initialize the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(text: str):
    return model.encode(text)
