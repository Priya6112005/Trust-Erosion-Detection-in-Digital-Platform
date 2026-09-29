def compute_trust_score(sentiment, behavior, interaction):

    # Weighted combination
    final_score = (
        sentiment * 0.3 +
        behavior * 0.4 +
        interaction * 0.3
    )

    return round(final_score, 2)