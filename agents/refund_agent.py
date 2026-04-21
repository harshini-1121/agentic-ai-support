from guardrails import check_refund_limit

def handle_refund(query):
    amount = 5000  # simulate extracted value

    if not check_refund_limit(amount):
        return "⚠️ Refund exceeds limit. Escalating to human agent."

    return "💰 Refund processed successfully."