import chromadb

client = chromadb.PersistentClient(path=".chroma")

collections = client.list_collections()
for col in collections:
    print(col)

aiderrag = client.get_collection("aider_rag")

print(aiderrag.get()["documents"][:10])

