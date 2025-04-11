from llama_index.llms.ollama import Ollama as ollm
from text import text_generator
from image import generate_image
from web_searcher import search_web
from filecreator import create_pptx_file

llm_head = ollm(model="phi", request_timeout=60.0)


prompt = input("Hey, How may I help you?")

task_steps = llm_head.complete("""Can you divide this task into a step-by-step format? Each step must be separated by a comma, and there must be no other commas inside any step. Do not include any other text before or after the steps.

DO NOT group similar tasks together—each step must be separate and sequential.
DO NOT include extra commentary, explanations, or follow-ups—ONLY provide the steps in the requested format.

**Only include essential and technical points—skip obvious steps like saving files or opening software**.

DO NOT provide multiple options for any step—just select the best one and go with it.

Now, process the following task:""" + prompt)

categorized_steps = llm_head.complete(f"""Assign a category to each step using the following format:

text_gen → For text generation tasks
image_gen → For image generation tasks
web_surfer → For web research tasks
ppt_gen → For PowerPoint slide creation
nil → If none of the above categories fit

Every task must be labeled with its category. Example: task 1 - Generate an introduction (text_gen).

Now categorize the following steps:""" + task_steps.text)


text = categorized_steps.text

splitted_task = text.split("\n")
print("\033[92m" + "\n".join(splitted_task) + "\033[0m")  # Print in green color
searched_results = ""
generated_text = ""


i = 0
while i < len(splitted_task):
    if "text_gen" in splitted_task[i]:
        print("generated text")
        generated_text = text_generator(splitted_task[i]+ "for"+ prompt).text
        print(generated_text)
    elif "image_gen" in splitted_task[i]:
        print("generated image")
        generate_image(splitted_task[i] + "for" + prompt)
    elif "web_surfer" in splitted_task[i]:
        print("generated web search")
        searched_results = search_web(splitted_task[i] + "for" + prompt)
        print(searched_results)
    elif "ppt_gen" in splitted_task[i]:
        print("generated ppt")
        create_pptx_file(prompt, "presentation.pptx")
    i += 1





