from chunking import clean_text, chunk_text
from rag_handler import VectorStorage

# Example document (replace with your actual content)
long_document = """The Nonnecessity of Marketing
Here is the biggest and most obvious difference between quantitative trading and other small businesses... (the sample text from your chunking.py)"""

# Initialize RAG system
vs = VectorStorage()

# Process document
cleaned = clean_text(long_document)
chunks = chunk_text(cleaned)
print(f"Chunked document into {len(chunks)} chunks")

# Store in vector DB
vs.store_chunks(chunks)

# Query example
query = "What are the main differences between quantitative trading and other businesses?"
context = vs.query_context(query)
print("\nRetrieved Context:")
print("\n".join(context))
