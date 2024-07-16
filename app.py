import os
import random
import openai
from llama_index.callbacks.base import CallbackManager
from llama_index import VectorStoreIndex
from llama_index.vector_stores import DeepLakeVectorStore
from llama_index.readers.deeplake import DeepLakeReader
from langchain.chat_models import ChatOpenAI
import chainlit as cl
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
activeloop_token = os.getenv('ACTIVELOOP_TOKEN')
activeloop_organization = os.getenv('ACTIVELOOP_ORGANIZATION')
dataset_name = os.getenv('DATASET_NAME')

os.environ['OPENAI_API_KEY'] = openai.api_key
os.environ["ACTIVELOOP_TOKEN"] = activeloop_token

dataset_path = f'hub://{activeloop_organization}/{dataset_name}'

def reload_llamaindex_index() -> VectorStoreIndex:
    query_vector = [random.random() for _ in range(1536)]
    reader = DeepLakeReader()
    documents = reader.load_data(query_vector=query_vector, dataset_path=dataset_path)
    return VectorStoreIndex.from_documents(documents)

index = reload_llamaindex_index()

@cl.llama_index_factory
def factory():
    return index.as_query_engine()

@cl.on_chat_start
async def start():
    await cl.Message(content="Welcome to the Alma Documentation Chatbot! How can I help you today?").send()

if __name__ == "__main__":
    cl.run()
