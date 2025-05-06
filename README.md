# 🇮🇳 Indian Legal MCP Assistant

**A multilingual legal chatbot powered by Retrieval-Augmented Generation (RAG) and Groq's LLaMA3**, designed to help Indian citizens understand key laws from IPC, CrPC, Evidence Act, and more.

---

## 🚀 Features

- 🧠 **Multi-act legal support** (IPC, CrPC, CPC, IEA, HMA, IDA, NIA)
- 📦 **RAG-based retrieval** from structured legal datasets
- 🧾 **Explains Indian law** with real sections, no hallucination
- 🌐 **Supports English, Tamil, and Hindi**
- ⚖️ Gradio-powered interactive UI
- 💬 Answers everyday questions (traffic rules, FIRs, landlord issues, consumer rights)

---

## 📁 Project Structure

```
legal_mcp_assistant/
├── app.py                    # Gradio UI
├── mcp_client.py             # Core LLM + RAG logic
├── requirements.txt
├── data/                     # JSON files for each Act
│   ├── ipc.json
│   ├── crpc.json
│   ├── ...
├── servers/                  # Each law server handles its own Act
│   ├── ipc_server.py
│   ├── crpc_server.py
│   ├── ...
```

---

## 🛠 Setup Instructions

```bash
# Clone repo and install dependencies
pip install -r requirements.txt

# Set your Groq API key
export GROQ_API_KEY=your-key-here  # or use dotenv

# Run the app
python app.py
```

Open `http://127.0.0.1:7860` in your browser.

---

## 💡 Example Queries

- "What is Section 138 of NIA?"
- "Can police arrest without a warrant?"
- "What if someone threatens me on WhatsApp?"
- "Do I need to wear a helmet inside city limits?"

---

## 📚 Acts Included

- Indian Penal Code (IPC)
- Code of Criminal Procedure (CrPC)
- Indian Evidence Act (IEA)
- Hindu Marriage Act (HMA)
- Indian Divorce Act (IDA)
- Code of Civil Procedure (CPC)
- Negotiable Instruments Act (NIA)

---

## 🤖 Powered By

- [Groq](https://groq.com/)
- [LLaMA3](https://llama.meta.com/)
- [Gradio](https://gradio.app/)
- Python 3.10+

---

## 📄 License

MIT — Use it, remix it, just don't break the law. 😄
