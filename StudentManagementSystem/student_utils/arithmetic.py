"""Arithmetic utilities for students."""
def percentage(scores):
    """Calculates percentage from a list of marks."""
    if not scores:
        return 0.0
    total = sum(scores)
    return round(total / (len(scores) * 100) * 100, 2)


def classify_grade(score):
    """Classifies a numeric score into a letter grade."""
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'