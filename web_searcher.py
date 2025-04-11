from duckduckgo_search import DDGS
from sentence_transformers import SentenceTransformer
import numpy as np

def search_web(query):

    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
        # Extract only the 'body' (text) from the results
        web_text_results = [result['body'] for result in results]
    
    return web_text_results
