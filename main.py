from llama_index.llms.ollama import Ollama
from llama_index.core import SimpleDirectoryReader, Document, VectorStoreIndex,Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

print('Loading documents...')
documents = SimpleDirectoryReader(
    input_files=["./eBook-How-to-Build-a-Career-in-AI.pdf"]
).load_data()
print(f"Loaded {len(documents)} documents")

# Basic RAG pipeline

document = Document(text="\n\n".join([doc.text for doc in documents]))
print(document.text[:1000])
# print(document.text[::400])

llm = Ollama(model="llama3.1", request_timeout=300.0, temperature=0.1)
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

Settings.llm = llm
Settings.embed_model = embed_model

print("Creating index...")
index = VectorStoreIndex.from_documents(documents)
print("Index created successfully.")


print("Creating query engine...")
query_engine = index.as_query_engine(streaming=True)
print("Query engine created. Ready to ask questions.")


print("\nQuerying...")
response = query_engine.query("Give me 3 pleases of advices how to get knowledge ")


print("\nResponse:")
print(response)
