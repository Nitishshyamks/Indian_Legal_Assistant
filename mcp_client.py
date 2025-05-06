import requests
import os

# Import from the servers module
from servers.ipc_server import IndianPenalCodeServer
from servers.crpc_server import CodeofCriminalProcedureServer
from servers.cpc_server import CodeofCivilProcedureServer
from servers.iea_server import IndianEvidenceActServer
from servers.hma_server import HinduMarriageActServer
from servers.ida_server import IndianDivorceActServer
from servers.nia_server import NegotiableInstrumentsActServer

# Initialize each server
ipc = IndianPenalCodeServer(data_path="data/ipc.json")
crpc = CodeofCriminalProcedureServer(data_path="data/crpc.json")
cpc = CodeofCivilProcedureServer(data_path="data/cpc.json")
iea = IndianEvidenceActServer(data_path="data/iea.json")
hma = HinduMarriageActServer(data_path="data/hma.json")
ida = IndianDivorceActServer(data_path="data/ida.json")
nia = NegotiableInstrumentsActServer(data_path="data/nia.json")

def build_context_blocks(user_query):
    return [
        {"type": "query", "content": user_query},
        {"type": "ipc", "content": "\n".join([f"{s.get('id', 'N/A')}: {s.get('title', '')} - {s.get('context', '')}" for s in ipc.search(user_query)])},
        {"type": "crpc", "content": "\n".join([f"{s.get('id', 'N/A')}: {s.get('title', '')} - {s.get('context', '')}" for s in crpc.search(user_query)])},
        {"type": "cpc", "content": "\n".join([f"{s.get('id', 'N/A')}: {s.get('title', '')} - {s.get('context', '')}" for s in cpc.search(user_query)])},
        {"type": "iea", "content": "\n".join([f"{s.get('id', 'N/A')}: {s.get('title', '')} - {s.get('context', '')}" for s in iea.search(user_query)])},
        {"type": "hma", "content": "\n".join([f"{s.get('id', 'N/A')}: {s.get('title', '')} - {s.get('context', '')}" for s in hma.search(user_query)])},
        {"type": "ida", "content": "\n".join([f"{s.get('id', 'N/A')}: {s.get('title', '')} - {s.get('context', '')}" for s in ida.search(user_query)])},
        {"type": "nia", "content": "\n".join([f"{s.get('id', 'N/A')}: {s.get('title', '')} - {s.get('context', '')}" for s in nia.search(user_query)])}
    ]

def translate_if_needed(text, lang):
    if lang == "Tamil":
        return "⚠️ மொழிபெயர்ப்பு தேவைக்கேற்ப சேர்க்கப்படலாம்: " + text
    elif lang == "Hindi":
        return "⚠️ यह उत्तर हिंदी में अनुवाद किया जा सकता है: " + text
    return text

def call_model(prompt_blocks):
    api_key = os.getenv("GROQ_API_KEY", "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")
    messages = [
        {"role": "system", "content": "You are a senior Indian criminal lawyer. Reply clearly and concisely with applicable sections from IPC, CrPC, and Evidence Act. Structure your answer using bullet points or short paragraphs for clarity."},
        {"role": "user", "content": "\n\n".join([f"[{blk['type'].upper()}]\n{blk['content']}" for blk in prompt_blocks if blk['content']])}
    ]

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"model": "llama3-70b-8192", "messages": messages, "temperature": 0.7}
    )

    if response.status_code != 200:
        raise Exception("Groq API error: " + response.text)
    return response.json()["choices"][0]["message"]["content"]

def mcp_query(user_input: str, lang="English"):
    blocks = build_context_blocks(user_input)
    output = call_model(blocks)
    return translate_if_needed(output, lang)
