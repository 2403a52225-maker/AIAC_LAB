def calculate_percentage(amount: float, percentage: float) -> float:
    """
    Calculate the percentage value of a given amount.

    Args:
        amount (float): The base amount.
        percentage (float): The percentage to calculate.

    Returns:
        float: The calculated percentage value.
    """
    return amount * percentage / 100

amount: float = 200
percentage: float = 15

result: float = calculate_percentage(amount, percentage)
print(result)