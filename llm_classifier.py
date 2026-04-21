import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROK_API_KEY"),
    base_url="https://api.x.ai/v1"
)

def classify_query_llm(query: str):
    """
    Simulates LLM-based intent classification using semantic patterns.
    Acts as a fallback when real LLM APIs are unavailable.
    """

    q = query.lower()

    # semantic understanding (not just simple keywords)
    order_patterns = [
        "where is my order", "track", "delivery", "shipped",
        "order status", "package", "when will i get"
    ]

    refund_patterns = [
        "refund", "return", "money back",
        "cancel order", "replacement", "wrong item"
    ]

    # intent detection
    if any(p in q for p in order_patterns):
        return "order"

    elif any(p in q for p in refund_patterns):
        return "refund"

    else:
        return "faq"