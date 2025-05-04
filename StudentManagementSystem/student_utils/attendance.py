"""Attendance utilities for students."""
def attendance_percentage(present, total):
    """Calculates attendance percentage."""
    if total == 0:
        return 0.0
    return round((present / total) * 100, 2)