import asyncio
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llama_index.core import SimpleDirectoryReader, Document, VectorStoreIndex,Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


print('Loading documents...')
documents = SimpleDirectoryReader(
    input_files=["./eBook-How-to-Build-a-Career-in-AI.pdf"]
).load_data()
print(f"Loaded {len(documents)} documents")

# Basic RAG pipeline

document = Document(text="\n\n".join([doc.text for doc in documents]))

# print(document.text[::400])

llm = ChatOllama(model="llama3.1", temperature=0.1)
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

Settings.llm = llm
Settings.embed_model = embed_model

print("Creating index...")
index = VectorStoreIndex.from_documents(documents)
print("Index created successfully.")


print("Creating query engine...")
query_engine = index.as_query_engine()
print("Query engine created. Ready to ask questions.")


print("\nQuerying...")
response = query_engine.query("What is the main topic of this book?")

print("\nResponse:")
print(response)


# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant."),
#     ("user", "{input}")
# ])
# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser
#
#
# async def get_streamed_response():
#     print("Assistant: ", end="", flush=True)
#
#     async for chunk in chain.astream({"input": "What's the recipe for a good omelette?"}):
#         print(chunk, end="", flush=True)
#     print()
#
#
# async def main():
#     await get_streamed_response()
#
#
# if __name__ == "__main__":
#     asyncio.run(main())