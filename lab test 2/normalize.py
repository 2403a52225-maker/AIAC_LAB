# normalize.py
from typing import List

def normalize(scores: List[float]) -> List[float]:
    """Normalize a list of numeric scores to the range [0, 1].

    This function rescales the input values so that the minimum maps to 0.0
    and the maximum maps to 1.0. Values in between are scaled linearly.
    The function also handles edge cases such as empty input or when all
    values are equal (to avoid divide-by-zero).

    Args:
        scores (List[float]): A list of numeric scores (int or float).

    Returns:
        List[float]: A list of normalized values in [0, 1].
        - If the input list is empty, returns [].
        - If all scores are equal, returns a list of 0.0 values
          with the same length as input.

    Examples:
        >>> normalize([10, 20, 30])
        [0.0, 0.5, 1.0]

        >>> normalize([5, 5, 5])
        [0.0, 0.0, 0.0]

        >>> normalize([])
        []

        >>> normalize([2])
        [0.0]
    """
    if not scores:
        return []
    m = max(scores)
    n = min(scores)
    if m == n:
        return [0.0] * len(scores)
    return [(x - n) / (m - n) for x in scores]


# Quick CLI for manual check
if __name__ == "__main__":
    sample_cases = [
        [10, 20, 30],
        [5, 5, 5],
        [],
        [2],
    ]
    for case in sample_cases:
        print(f"{case} -> {normalize(case)}")
        # INSERT_YOUR_CODE
        # Take input from the console, normalize, and print result
        inp = input("Enter numbers separated by spaces: ").strip()
        if inp:
            try:
                nums = [float(x) for x in inp.split()]
                print(f"Normalized: {normalize(nums)}")
            except ValueError:
                print("Invalid input: please enter numbers only.")
                # INSERT_YOUR_CODE

