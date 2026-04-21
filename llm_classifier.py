import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def classify_query_llm(query: str):
    try:
        prompt = f"""
        Classify the query into one of:
        - order
        - refund
        - faq

        Return only one word.

        Query: {query}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text.strip().lower()

    except Exception as e:
        print("⚠️ Gemini failed, using fallback:", e)

        q = query.lower()
        if "order" in q or "track" in q:
            return "order"
        elif "refund" in q or "return" in q:
            return "refund"
        else:
            return "faq"