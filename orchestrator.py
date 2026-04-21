from llm_classifier import classify_query_llm
from monitor import log_event


def route_query(query: str):
    intent = classify_query_llm(query)

    log_event(f"Query: {query}")
    log_event(f"Detected intent: {intent}")

    if "order" in intent:
        from agents.order_agent import handle_order
        log_event("Routed to Order Agent")
        return handle_order(query)

    elif "refund" in intent:
        from agents.refund_agent import handle_refund
        log_event("Routed to Refund Agent")
        return handle_refund(query)

    else:
        from agents.faq_agent import handle_faq
        log_event("Routed to FAQ Agent")
        return handle_faq(query)