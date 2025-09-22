def calculate_average(scores):
    """
    Calculate the average of a list of numerical scores.

    Args:
        scores (list of int or float): List containing the scores.

    Returns:
        float: The average score.

    Raises:
        ValueError: If the scores list is empty.
    """
    if not scores:
        raise ValueError("The scores list cannot be empty.")
    return sum(scores) / len(scores)

student_scores = [85, 90, 78, 92]
print("Average Score is", calculate_average(student_scores))