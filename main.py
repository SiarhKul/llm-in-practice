import asyncio
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="llama3.1")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


async def get_streamed_response():
    print("Assistant: ", end="", flush=True)

    async for chunk in chain.astream({"input": "What's the recipe for a good omelette?"}):
        print(chunk, end="", flush=True)
    print()


async def main():
    await get_streamed_response()


if __name__ == "__main__":
    asyncio.run(main())