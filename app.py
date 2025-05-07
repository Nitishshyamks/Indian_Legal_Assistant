import gradio as gr
from mcp_client import mcp_query

def respond(query, lang):
    return mcp_query(query, lang=lang)

with gr.Blocks(theme=gr.themes.Soft(primary_hue="violet"), css="""
#title { text-align: center; font-size: 28px; font-weight: bold; color: #4B0082; margin-top: 12px; }
#footer { text-align: center; font-size: 13px; color: #555; margin-top: 1.5rem; }
""") as demo:
    gr.Markdown("## ⚖️ Vakil.Aiyya – Your Friendly Legal Assistant 🇮🇳", elem_id="title")

    with gr.Row():
        with gr.Column(scale=3):
            user_input = gr.Textbox(label="🔍 Ask a Legal Question", placeholder="Stuck with a police case or court term? Type it. We simplify it.", lines=2)
            language = gr.Dropdown(["English", "Tamil", "Hindi"], value="English", label="🌐 Choose Language")
            submit_btn = gr.Button("⚖️ Get Answer")
        with gr.Column(scale=5):
            response = gr.Textbox(label="📜 Legal Explanation", lines=15, interactive=False)

    gr.Markdown("🤝 Know your rights. Ask better. Live safer. 🇮🇳", elem_id="footer")

    submit_btn.click(fn=respond, inputs=[user_input, language], outputs=response)

demo.launch(share=True)
