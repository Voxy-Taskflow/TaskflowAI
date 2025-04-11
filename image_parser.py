from llama_index.llms.ollama import Ollama as ollm
from PIL import Image
import base64
import requests

# Load LLaVA model
llm_vision = ollm(model="llava", request_timeout=30.0)

# Function to encode image for LLaVA
def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Function to process image with LLaVA
def process_image(image_path, prompt):
    image_data = encode_image(image_path)
    result = llm_vision.complete(f"{prompt} <image>{image_data}</image>")
    return result
