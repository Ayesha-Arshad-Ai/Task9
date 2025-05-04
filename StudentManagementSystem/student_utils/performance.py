"""Performance evaluation utilities for students."""
def evaluate_performance(gpa):
    """Returns performance category based on GPA."""
    if gpa >= 3.5: return 'Excellent'
    if gpa >= 3.0: return 'Good'
    if gpa >= 2.0: return 'Average'
    return 'Needs Improvement'
