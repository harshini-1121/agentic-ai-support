from llm_classifier import classify_query_llm
from monitor import log_event

def route_query(query: str):
    intent = classify_query_llm(query)

    log_event(f"Query: {query}")
    log_event(f"Intent: {intent}")

    if intent == "order":
        from agents.order_agent import handle_order
        return handle_order(query)

    elif intent == "refund":
        from agents.refund_agent import handle_refund
        return handle_refund(query)

    else:
        from agents.faq_agent import handle_faq
        return handle_faq(query)