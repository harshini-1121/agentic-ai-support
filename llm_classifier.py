from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(token=os.getenv("HF_API_KEY"))

LABELS = ["order", "refund", "faq"]

def classify_query_llm(query: str):
    try:
        result = client.zero_shot_classification(
            query,
            candidate_labels=LABELS,
            model="facebook/bart-large-mnli"
        )

        # Case 1: dict with labels
        if isinstance(result, dict) and "labels" in result:
            return result["labels"][0]

        # Case 2: list of label-score dicts
        elif isinstance(result, list):
            return result[0]["label"]

        else:
            return "faq"

    except Exception as e:
        print("⚠️ HF failed:", e)
        return "faq"