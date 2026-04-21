REFUND_LIMIT = 3000


def check_refund_limit(amount):
    if amount > REFUND_LIMIT:
        return False
    return True


def prevent_sensitive_data(text):
    if "credit card" in text.lower():
        return False
    return True