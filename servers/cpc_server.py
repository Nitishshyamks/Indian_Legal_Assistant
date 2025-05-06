import json
import os

class CodeofCivilProcedureServer:
    def __init__(self, data_path="data_new/cpc.json"):
        with open(data_path, "r", encoding="utf-8") as f:
            self.sections = json.load(f)

    def search(self, query):
        query = query.lower()
        results = []
        for entry in self.sections:
            if (
                str(entry.get("id", "")).lower() in query
                or query in entry.get("title", "").lower()
                or query in entry.get("context", "").lower()
            ):
                results.append(entry)
        return results[:5]