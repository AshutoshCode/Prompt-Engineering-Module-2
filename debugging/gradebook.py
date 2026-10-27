"""Gradebook helpers (FIXED version for Assignment 8)."""


def average(marks):
    """Mean of marks; 0.0 for an empty list instead of crashing."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def add_mark(mark, marks=None):
    """Append mark to marks. A new list is made per call when none is given."""
    if marks is None:
        marks = []
    marks.append(mark)
    return marks


def letter_grade(score):
    """A >= 90, B >= 75, C >= 50, otherwise F (boundaries are inclusive)."""
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    return "F"


def highest(marks):
    """Largest mark; raises ValueError for an empty list."""
    if not marks:
        raise ValueError("highest() needs at least one mark")
    best = marks[0]
    for m in marks[1:]:
        if m > best:
            best = m
    return best


def remove_failing(marks, pass_mark=40):
    """Return a new list without marks below pass_mark (input is not modified)."""
    return [m for m in marks if m >= pass_mark]
