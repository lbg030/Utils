import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


from diffusers import StableDiffusionPipeline
import torch

model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16")

# pipe = pipe.to("cuda")

prompt = "a photo of an programmer riding a computer on desk"
image = pipe(prompt).images[0]

image.save("test.png")
