def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def factorial(n):
    """Return the factorial of a non-negative integer n.

    The factorial of 0 is 1. For negative n a ValueError is raised.
    A TypeError is raised if n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
