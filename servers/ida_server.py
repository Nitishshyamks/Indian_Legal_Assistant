import numpy as np
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class IndianDivorceActServer:
    def __init__(self,
                 emb_path="Data_emb_npy/ida_embeddings.npy",
                 meta_path="Data_emb_json/ida_metadata.json",
                 model_name="all-MiniLM-L6-v2"):

        # Load embeddings and metadata
        self.embeddings = np.load(emb_path)
        with open(meta_path, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        # Load semantic model
        self.model = SentenceTransformer(model_name)

    def search(self, query, top_k=5):
        # Convert query to embedding
        query_embedding = self.model.encode(query, convert_to_numpy=True)

        # Compute similarity
        similarities = cosine_similarity([query_embedding], self.embeddings)[0]
        top_indices = similarities.argsort()[::-1][:top_k]

        # Return top matches
        return [self.metadata[i] for i in top_indices]
