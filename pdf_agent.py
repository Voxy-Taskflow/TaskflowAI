from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.core.embeddings import resolve_embed_model
from text import ollm
from api import parser_api

parser = LlamaParse(result_type="markdown")
file_extractor = {".pdf" : parser}
documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data

embed_model1 = resolve_embed_model("local:BAAI/bge-m3")
vector_index = VectorStoreIndex.from_documents(documents=documents, embed_model=embed_model1)
query_engine = vector_index.as_query_engine(llm=ollm)

def pdf_scraper(query):
    result = query_engine.query(query)
    return result
