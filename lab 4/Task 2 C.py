def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.
    Returns 'not defined' for negative inputs.
    """
    if n < 0:
        return "not defined"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(-5))