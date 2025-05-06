import gradio as gr
from mcp_client import mcp_query

def respond(query, lang):
    return mcp_query(query, lang=lang)

with gr.Blocks(theme=gr.themes.Soft(primary_hue="violet")) as demo:
    gr.Markdown("## 🧑‍⚖️ Indian Legal Assistant", elem_id="title")
    with gr.Row():
        with gr.Column(scale=3):
            user_input = gr.Textbox(label="🔍 Ask a Legal Question", placeholder="e.g. What is IPC 302 or Bail law?", lines=2)
            language = gr.Radio(["English", "Tamil", "Hindi"], label="🌐 Choose Language", value="English")
            submit_btn = gr.Button("⚖️ Get Answer")
        with gr.Column(scale=5):
            response = gr.Textbox(label="📜 Legal Explanation", lines=15, interactive=False)
    gr.Markdown("Made with 🧠 Groq + Indian Law Acts | 🇮🇳")

    submit_btn.click(fn=respond, inputs=[user_input, language], outputs=response)

demo.launch()