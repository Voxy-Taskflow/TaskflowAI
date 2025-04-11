from llama_index.llms.ollama import Ollama as ollm


llm = ollm(model="mistral", request_timeout=60.0)

def text_generator(query):
    result = llm.complete(query)
    return result

