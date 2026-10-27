"""Struct-based program: Python version of c_programs/student_struct.c."""
from dataclasses import dataclass


@dataclass
class Student:
    roll: int
    name: str
    marks: float


def main() -> None:
    students = [
        Student(1, "Asha", 82.5),
        Student(2, "Ravi", 74.0),
        Student(3, "Meera", 91.25),
    ]
    for s in students:
        print(f"Roll {s.roll}: {s.name:<6} {s.marks:.2f}")
    average = sum(s.marks for s in students) / len(students)
    topper = max(students, key=lambda s: s.marks)
    print(f"Average marks: {average:.2f}")
    print(f"Topper: {topper.name} ({topper.marks:.2f})")


if __name__ == "__main__":
    main()
