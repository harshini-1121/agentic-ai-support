from guardrails import check_refund_limit
from monitor import log_event

def handle_refund(query):
    amount = 5000

    if not check_refund_limit(amount):
        log_event("Guardrail triggered: refund limit exceeded")
        return " Refund exceeds limit. Escalating to human agent."

    return " Refund processed successfully."