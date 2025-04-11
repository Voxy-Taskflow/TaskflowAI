import pandas as pd
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from llama_index.llms.ollama import Ollama as ollm

#def create_csv_file(data, file_name):
    #"""
    #Create a CSV file with the given data and file name.

    #:param data: List of dictionaries or pandas DataFrame to write to CSV.
    #:param file_name: Name of the CSV file to create.
    #"""
    #if isinstance(data, list):
    #    df = pd.DataFrame(data)
    #elif isinstance(data, pd.DataFrame):
     #   df = data
    #else:
     #   raise ValueError("Data must be a list of dictionaries or a pandas DataFrame.")
    
    #df.to_csv(file_name, index=False)
    #print(f"CSV file '{file_name}' created successfully.")

def create_txt_file(content, file_name):
    """
    Create a TXT file with the given content and file name.

    :param content: String content to write to the TXT file.
    :param file_name: Name of the TXT file to create.
    """
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"TXT file '{file_name}' created successfully.")

def create_pptx_file(slides_content, file_name):
    """
    Create a PPTX file with the given slides content and file name.
    """
    # Get Content for the PPT
    llm = ollm(model="phi", request_timeout=60.0)
    simpplified_text = llm.complete("simplify this text to make it more concise and clear: " + slides_content)
    print("\033[92m" + simpplified_text.text + "\033[0m")

    # Updated prompt to handle the new format
    formated_text = llm.complete("""Convert the following slide information into this exact format:
[Slide Title] | [Slide Content] | [Font Size Number Only] | [LEFT/CENTER/RIGHT]

Rules:
1. Each slide should be separated by a semicolon (;)
2. Remove "pt" from font sizes, keep only the number
3. Keep alignments in uppercase
4. Include meaningful content for each slide based on its title
5. DO NOT include any other text or explanations

For example:
Input:
Slide 1: Introduction
Font Size: 12pt
Text Alignment: Center

Output:
Slide 1: Introduction|This is an introduction to our topic|12|CENTER

Now format the following content:
""" + simpplified_text.text)
    
    print("\033[92m" + formated_text.text + "\033[0m")
    
    # Rest of the existing code remains the same
    text = formated_text.text

    # Parse the input text into slides
    slides = []
    current_slide = {}
    
    # Split the content into lines
    lines = text.split(';')
    
    for line in lines:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
            
        parts = line.split("|")
        current_slide = {
            "title": parts[0].strip(),
            "content": parts[1].strip(),
            "font_size": int(parts[2].strip()),
            "alignment": getattr(PP_ALIGN, parts[3].strip(), PP_ALIGN.LEFT)
        }
        slides.append(current_slide)

    # Create the presentation
    presentation = Presentation()
    for slide_data in slides:
        slide = presentation.slides.add_slide(presentation.slide_layouts[5])  # Blank slide layout

        # Extract slide data
        title = slide_data.get("title", "")
        content = slide_data.get("content", "")
        font_size = slide_data.get("font_size", 18)
        alignment = slide_data.get("alignment", PP_ALIGN.LEFT)

        # Add title
        title_box = slide.shapes.add_textbox(left=Inches(1), top=Inches(0.5), width=Inches(8), height=Inches(1))
        title_frame = title_box.text_frame
        title_frame.text = title
        title_frame.paragraphs[0].font.size = Pt(28)
        title_frame.paragraphs[0].font.bold = True

        # Add content
        content_box = slide.shapes.add_textbox(left=Inches(1), top=Inches(1.5), width=Inches(8), height=Inches(5))
        content_frame = content_box.text_frame
        content_frame.text = content
        content_frame.paragraphs[0].font.size = Pt(font_size)
        content_frame.paragraphs[0].alignment = alignment

    # Save the presentation
    presentation.save(f"{file_name}.pptx")
    print(f"PPTX file '{file_name}.pptx' created successfully.")