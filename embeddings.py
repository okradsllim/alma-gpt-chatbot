import os
import tempfile
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext, StorageContext, DeepLakeVectorStore
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
activeloop_token = os.getenv('ACTIVELOOP_TOKEN')
activeloop_organization = os.getenv('ACTIVELOOP_ORGANIZATION')
dataset_name = os.getenv('DATASET_NAME')

os.environ['OPENAI_API_KEY'] = openai.api_key
os.environ["ACTIVELOOP_TOKEN"] = activeloop_token

dataset_path = f'hub://{activeloop_organization}/{dataset_name}'
docs_dir = "alma_docs"

llm_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
llm_predictor = LLMPredictor(llm=llm_model)
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
storage_context = StorageContext.from_defaults(vector_store=DeepLakeVectorStore(dataset_path=dataset_path, overwrite=True))

def create_embeddings():
    filename_fn = lambda filename: {'file_name': filename}
    documents = SimpleDirectoryReader(docs_dir, file_metadata=filename_fn).load_data()
    VectorStoreIndex.from_documents(documents, service_context=service_context, storage_context=storage_context)

if __name__ == "__main__":
    create_embeddings()
    print("Embeddings created and stored in the database.")
