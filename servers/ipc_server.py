import numpy as np
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class IndianPenalCodeServer:
    def __init__(self,
                 emb_path="Data_emb_npy/ipc_embeddings.npy",
                 meta_path="Data_emb_json/ipc_metadata.json",
                 model_name="all-MiniLM-L6-v2"):

        # Load section metadata and precomputed embeddings
        self.embeddings = np.load(emb_path)
        with open(meta_path, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        # Load transformer model
        self.model = SentenceTransformer(model_name)

    def search(self, query, top_k=5):
        # Encode query into vector
        query_embedding = self.model.encode(query, convert_to_numpy=True)

        # Calculate similarity scores
        similarities = cosine_similarity([query_embedding], self.embeddings)[0]
        top_indices = similarities.argsort()[::-1][:top_k]

        # Return top matches
        return [self.metadata[i] for i in top_indices]
