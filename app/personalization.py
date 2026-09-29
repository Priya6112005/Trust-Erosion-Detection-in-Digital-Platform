# app/personalization.py

# For each detected reason, explain to the MANAGER what the customer
# likely experienced, and what the manager should do about it.
PERSONALIZATION_RULES = {
    "Negative sentiment detected": {
        "primary_issue": "negative_sentiment",
        "customer_problem": (
            "The customer's messages/text showed frustration or dissatisfaction "
            "during their session — something about their experience upset them."
        ),
        "recommended_action": (
            "Review this customer's recent messages or support chat to understand "
            "what went wrong, and consider reaching out personally to resolve it."
        ),
    },
    "Checkout abandonment detected": {
        "primary_issue": "checkout_abandonment",
        "customer_problem": (
            "The customer added items to their cart or started checkout, but did "
            "not complete the purchase."
        ),
        "recommended_action": (
            "Check for friction in the checkout flow — unexpected shipping costs, "
            "a confusing payment step, or a technical error. Consider a follow-up "
            "offer or reminder."
        ),
    },
    "Multiple policy verification attempts": {
        "primary_issue": "multiple_policy_checks",
        "customer_problem": (
            "The customer repeatedly checked return, refund, or warranty policy "
            "pages — a sign they were unsure or hesitant to trust the purchase."
        ),
        "recommended_action": (
            "Make your return/refund/warranty policies clearer and easier to find "
            "on product pages, so customers don't need to search for reassurance."
        ),
    },
    "High hesitation time during checkout": {
        "primary_issue": "high_hesitation_time",
        "customer_problem": (
            "The customer spent an unusually long time deciding during checkout, "
            "which often signals confusion, price hesitation, or comparison shopping."
        ),
        "recommended_action": (
            "Consider adding clearer product comparisons, reviews, or a live chat "
            "option at checkout to reduce hesitation."
        ),
    },
}


# Fallback used if no known reason matches
DEFAULT_PERSONALIZATION = {
    "primary_issue": "general_concern",
    "customer_problem": "A general trust erosion signal was detected for this customer.",
    "recommended_action": "Review this session's details manually to understand what happened.",
}


def get_personalization(reasons: list[str]) -> dict:
    """
    Takes the list of risk reasons detected by trust_score.py
    and returns an explanation of the customer's likely problem,
    plus a recommended action for the manager.
    """
    for reason in reasons:
        if reason in PERSONALIZATION_RULES:
            return PERSONALIZATION_RULES[reason]

    return DEFAULT_PERSONALIZATION