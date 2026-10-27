"""Factorial: Python version of c_programs/factorial.c."""


def factorial(n: int) -> int:
    """Return n! for n >= 0. Python ints do not overflow, so no upper limit."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main() -> None:
    for n in (0, 1, 5, 10, 20):
        print(f"{n}! = {factorial(n)}")


if __name__ == "__main__":
    main()
