import torch
import os
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq
from transformers.image_utils import load_image
import gradio as gr

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize processor and model
processor = AutoProcessor.from_pretrained("HuggingFaceTB/SmolVLM-Instruct")
model = AutoModelForVision2Seq.from_pretrained(
    "HuggingFaceTB/SmolVLM-Instruct",
    torch_dtype=torch.bfloat16,
    _attn_implementation="flash_attention_2" if DEVICE == "cuda" else "eager",
).to(DEVICE)

# Load available images from the folder
IMAGES_FOLDER = "plots/"
image_files = [f for f in os.listdir(IMAGES_FOLDER) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

def answer_question(image_file, question):
    # Load selected image
    image_path = os.path.join(IMAGES_FOLDER, image_file)
    image = load_image(image_path)
    
    # Create input messages
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": question},
            ]
        },
    ]

    # Prepare inputs
    prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(text=prompt, images=[image], return_tensors="pt").to(DEVICE)

    # Generate outputs
    generated_ids = model.generate(**inputs, max_new_tokens=500)
    generated_texts = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True,
    )

    return generated_texts[0]

# Define Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Vision-Language Model UI")
    with gr.Row():
        image_dropdown = gr.Dropdown(label="Select an Image", choices=image_files, value=image_files[0])
        question_input = gr.Textbox(label="Enter Your Question", placeholder="Type your question here...")
    with gr.Row():
        submit_button = gr.Button("Get Answer")
        output_text = gr.Textbox(label="Answer", interactive=False)
    
    submit_button.click(fn=answer_question, inputs=[image_dropdown, question_input], outputs=output_text)

# Launch Gradio app
demo.launch()
