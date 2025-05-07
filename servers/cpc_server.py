import numpy as np
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class CodeofCivilProcedureServer:
    def __init__(self,
                 emb_path="Data_emb_npy/cpc_emb.npy",
                 meta_path="Data_emb_json/cpc_metadata.json",
                 model_name="all-MiniLM-L6-v2"):
        
        # Load metadata and embeddings
        self.metadata = self._load_json(meta_path)
        self.embeddings = np.load(emb_path)

        # Load embedding model
        self.model = SentenceTransformer(model_name)

    def _load_json(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def search(self, query, top_k=5):
        # Encode the query
        query_embedding = self.model.encode(query, convert_to_numpy=True)

        # Compute cosine similarity
        similarities = cosine_similarity([query_embedding], self.embeddings)[0]
        top_indices = similarities.argsort()[::-1][:top_k]

        # Return top matching sections
        return [self.metadata[i] for i in top_indices]
