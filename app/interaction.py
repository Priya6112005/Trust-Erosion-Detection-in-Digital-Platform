def analyze_interaction(messages_count: int, dispute_flag: int):

    score = 100

    if dispute_flag == 1:
        score -= 50

    if messages_count < 2:
        score -= 20

    return max(score, 0)