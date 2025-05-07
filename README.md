
# 🧑‍⚖️ Vakil.Aiyya – Indian Legal Assistant

**Vakil.Aiyya** is a multilingual AI-powered legal assistant built using **Retrieval-Augmented Generation (RAG)** and **Model Context Protocol (MCP)**. It helps users understand Indian laws in a simple, clear, and interactive way. With deep support for **IPC**, **CrPC**, **CPC**, and more, it enables anyone to ask realistic legal queries in **English**, **Tamil**, or **Hindi** and receive structured, well-referenced responses.

---

## 🔍 Ask Real-World Questions Like

> - 🏍️ _"Is it illegal to ride a two-wheeler without a helmet in Tamil Nadu?"_  
> - 📝 _"What legal action can I take if my landlord increases rent suddenly?"_  
> - 💳 _"How do I file a complaint if someone misuses my debit card?"_  
> - 👮 _"Can police arrest without a warrant under CrPC?"_  
> - 💔 _"How can I get a divorce under the Hindu Marriage Act?"_  
> - 📜 _"What does IPC Section 420 actually say?"_  
> - 💰 _"Cheque bounced — what are my rights under the Negotiable Instruments Act?"_

---

## ⚙️ Features

- ✅ **RAG-based Legal Retrieval** from:
  - Indian Penal Code (IPC)
  - Code of Criminal Procedure (CrPC)
  - Code of Civil Procedure (CPC)
  - Indian Evidence Act (IEA)
  - Hindu Marriage Act (HMA)
  - Indian Divorce Act (IDA)
  - Negotiable Instruments Act (NIA)

- 🔤 **Multilingual Support**: English, Tamil, Hindi
- 🤖 **LLM-Powered Reasoning** via Groq’s LLaMA 3 (70B)
- ✍️ **Markdown-enhanced output** for clarity and visual structure
- 🧠 Context-aware responses using **MCP-style input blocks**
- ⚠️ Legal disclaimer checkbox and scroll-to-top UX
- 🎨 Themed Gradio UI with Indian flag colors

---

## 🧠 How It Works (MCP + RAG)

1. **Query** is analyzed and passed to multiple law-specific RAG servers.
2. **Each server** (IPC, CrPC, etc.) fetches relevant sections using semantic embeddings.
3. **MCP Client** builds a structured list of context blocks like:
   ```
   [QUERY] What is IPC 302?
   [IPC] Section 302: Punishment for murder – Whoever commits murder shall be punished with death or imprisonment...
   [CRPC] Section 154: Information in cognizable cases...
   ```
4. This block is sent to the **Groq LLM API** for generating a complete answer.
5. If user selects Tamil or Hindi, the final response is **translated** using `googletrans`.
6. Result is rendered as **scrollable Markdown HTML box** styled like a chat assistant.

---

## 📁 Project Structure

```
legal_mcp_assistant/
├── app.py                       ← Gradio UI
├── mcp_client.py               ← MCP + RAG + translation + LLM call
├── servers/                    ← Legal servers with vector search
│   ├── ipc_server.py
│   ├── crpc_server.py
│   └── ...                     ← hma, ida, nia, etc.
├── Data_emb_json/              ← Metadata for embeddings
├── Data_emb_npy/               ← NumPy embedding files
├── data_new/                   ← Base JSON files for all laws
├── requirements.txt
└── README.md
```

---

## 🚀 Running the App

```bash
git clone https://github.com/yourname/vakil-aiyya.git
cd vakil-aiyya
pip install -r requirements.txt
python app.py
```

App runs at `https://a21526c3df38b299f3.gradio.live` or gives you a public Gradio share link.

---

## 🔐 Authentication

Set your Groq API key:

```bash
export GROQ_API_KEY=your-groq-api-key
```

---

## 💬 Example Conversation

**Q:** _"Can I get bail under IPC 307?"_

**A:**  
> **IPC Section 307**: Attempt to murder  
> A person can apply for bail depending on the stage of investigation and gravity.  
> **CrPC Section 437** allows Magistrates to grant bail under specific conditions...  
> 📌 Bail may be denied if there's prior conviction or risk of influencing witnesses.

---

## 🧩 Credits

Built with 🧠 by [Codework.ai](https://codework.ai)

- UI: [Gradio](https://www.gradio.app)
- LLM API: [Groq Console](https://console.groq.com)
- Markdown: [`markdown2`](https://github.com/trentm/python-markdown2)
- Translation: [`googletrans`](https://pypi.org/project/googletrans)

---

Made for the people 🇮🇳 — not just the lawyers.

