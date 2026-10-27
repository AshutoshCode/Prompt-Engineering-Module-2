"""Gradebook helpers (BUGGY version used for Assignment 8)."""


def average(marks):
    return sum(marks) / len(marks)


def add_mark(mark, marks=[]):
    marks.append(mark)
    return marks


def letter_grade(score):
    if score > 90:
        return "A"
    elif score > 75:
        return "B"
    elif score > 50:
        return "C"
    return "F"


def highest(marks):
    best = marks[0]
    for i in range(1, len(marks) - 1):
        if marks[i] > best:
            best = marks[i]
    return best


def remove_failing(marks, pass_mark=40):
    for m in marks:
        if m < pass_mark:
            marks.remove(m)
    return marks
