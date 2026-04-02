import os
import gradio as gr
from groq import Groq

# Initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def translate_text(text):
    if not text.strip():
        return "Please enter text."

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert translator. Translate English to Urdu accurately. Only return translation."
                },
                {
                    "role": "user",
                    "content": f"Translate this into Urdu:\n{text}"
                }
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🌍 English → Urdu Translator")

    input_text = gr.Textbox(
        label="Enter English Text",
        placeholder="Type here...",
        lines=4
    )

    output_text = gr.Textbox(
        label="Urdu Translation",
        lines=4
    )

    btn = gr.Button("Translate")

    btn.click(translate_text, inputs=input_text, outputs=output_text)

# Launch (important for Colab)
demo.launch(share=True)