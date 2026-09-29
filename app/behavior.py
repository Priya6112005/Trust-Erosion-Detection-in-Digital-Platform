def analyze_behavior(abandonment: int, policy_checks: int, hesitation_time: int):

    score = 100

    if abandonment == 1:
        score -= 40

    score -= policy_checks * 10
    score -= hesitation_time * 0.2

    return max(score, 0)