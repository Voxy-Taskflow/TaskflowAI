# TaskflowAI

**TaskflowAI** is an intelligent task automation framework designed to break down complex tasks into actionable steps and execute them using specialized agents. It leverages cutting-edge AI models for natural language processing, image generation, web searching, PDF parsing, and more — making it a powerful assistant for developers, researchers, and productivity enthusiasts.

> ⚠️ **Note:** TaskflowAI is currently under active development and may not function as expected. Some features are buggy or incomplete.

---

## 🚀 Features

- 🧠 **Text Generation**: Summarize, outline, and generate detailed content using large language models.
- 🎨 **Image Generation**: Create high-quality images from textual prompts via Stable Diffusion.
- 🌐 **Web Searching**: Search the internet to collect relevant and up-to-date information.
- 📄 **PDF Parsing**: Extract and summarize content from PDF documents.
- 📊 **Presentation Creation**: Generate PowerPoint presentations from high-level task descriptions.
- 🖼️ **Image Parsing**: Extract text and structured data from images.
- ✅ **Task Categorization**: Automatically break down and classify complex tasks into executable steps.

---

## 🧹 Project Structure

```
TaskflowAI/
├── api.py                # API keys and configuration management
├── brain_data.jsonl      # Sample task data in JSONL format
├── filecreator.py        # File generation utilities (PPTX, TXT, etc.)
├── head.py               # Main entry point for task execution
├── image_parser.py       # Image processing and text extraction
├── image.py              # Image generation module
├── pdf_agent.py          # PDF parsing and querying logic
├── text.py               # Language model-based text generation
├── web_searcher.py       # Web search utility
├── data/                 # Directory for storing input/output data
├── dependencies/
│   └── requirements.txt  # Required Python packages
└── README.md             # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-repo/taskflow-ai.git
cd taskflow-ai
```

2. Install the required dependencies:

```bash
pip install -r dependencies/requirements.txt
```

3. Ensure you have the following APIs and models configured:

- **LlamaIndex** for text and PDF processing
- **Stable Diffusion** for image generation
- **DuckDuckGo Search API**

---

## ▶️ Usage

To use TaskflowAI:

```bash
python head.py
```

When prompted, enter your task. The system will:

1. Break the task into actionable steps
2. Categorize each step
3. Execute steps using the appropriate agents (text, image, PDF, etc.)

---

## 🔹 Example Tasks

- Create a presentation on AI advancements
- Generate a monthly sales report
- Design a futuristic city layout
- Write a blog post on healthy eating habits

---

## 📦 Dependencies

Make sure to install the following Python packages (already listed in `requirements.txt`):

- `fastapi`
- `uvicorn[standard]`
- `duckduckgo_search`
- `sentence_transformers`
- `llama_index`
- `diffusers`
- `torch`
- `Pillow`
- `python-pptx`
- `pandas`

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

