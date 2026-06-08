from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Chargement du modèle une seule fois

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(job_description, cv_text):


    if not job_description.strip():
        return 0

    job_embedding = model.encode([job_description])

    cv_embedding = model.encode([cv_text])

    similarity = cosine_similarity(
        job_embedding,
        cv_embedding
    )[0][0]

    return round(similarity * 100, 2)