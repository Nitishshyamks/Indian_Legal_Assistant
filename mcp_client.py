import requests
import os
import asyncio
from googletrans import Translator

# Import servers
from servers.ipc_server import IndianPenalCodeServer
from servers.crpc_server import CodeofCriminalProcedureServer
from servers.cpc_server import CodeofCivilProcedureServer
from servers.iea_server import IndianEvidenceActServer
from servers.hma_server import HinduMarriageActServer
from servers.ida_server import IndianDivorceActServer
from servers.nia_server import NegotiableInstrumentsActServer

# Initialize translator
translator = Translator()

# Initialize servers
ipc = IndianPenalCodeServer(
    emb_path="Data_emb_npy/ipc_emb.npy",
    meta_path="Data_emb_json/ipc_metadata.json"
)
crpc = CodeofCriminalProcedureServer(
    emb_path="Data_emb_npy/crpc_emb.npy",
    meta_path="Data_emb_json/crpc_metadata.json"
)
cpc = CodeofCivilProcedureServer(
    emb_path="Data_emb_npy/cpc_emb.npy",
    meta_path="Data_emb_json/cpc_metadata.json"
)
iea = IndianEvidenceActServer(
    emb_path="Data_emb_npy/iea_emb.npy",
    meta_path="Data_emb_json/iea_metadata.json"
)
hma = HinduMarriageActServer(
    emb_path="Data_emb_npy/hma_emb.npy",
    meta_path="Data_emb_json/hma_metadata.json"
)
ida = IndianDivorceActServer(
    emb_path="Data_emb_npy/ida_emb.npy",
    meta_path="Data_emb_json/ida_metadata.json"
)
nia = NegotiableInstrumentsActServer(
    emb_path="Data_emb_npy/nia_emb.npy",
    meta_path="Data_emb_json/nia_metadata.json"
)

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
    async def do_translate():
        if lang == "Tamil":
            return await translator.translate(text, dest='ta')
        elif lang == "Hindi":
            return await translator.translate(text, dest='hi')
        return None

    result = asyncio.run(do_translate())
    return result.text if result else text

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
    translated = translate_if_needed(output, lang)
    return translated
