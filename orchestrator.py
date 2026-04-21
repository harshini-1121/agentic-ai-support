from llm_classifier import classify_query_llm


def route_query(query: str):
    intent = classify_query_llm(query)

    print(f"🔍 Detected intent: {intent}")

    if "order" in intent:
        from agents.order_agent import handle_order
        return handle_order(query)

    elif "refund" in intent:
        from agents.refund_agent import handle_refund
        return handle_refund(query)

    else:
        from agents.faq_agent import handle_faq
        return handle_faq(query)