"""Fibonacci: Python version of c_programs/fibonacci.c."""


def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers: 0, 1, 1, 2, ..."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def main() -> None:
    print(" ".join(str(x) for x in fibonacci(10)))


if __name__ == "__main__":
    main()
