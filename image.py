from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt):
    print(f"[INFO] Generating image for: {prompt}")
    image = pipe(prompt).images[0]
    image_path = "generated_image.png"
    image.save(image_path)
    
    print(f"[SUCCESS] Image saved at {image_path}")
    return f"Image generated and saved at: {image_path}"
