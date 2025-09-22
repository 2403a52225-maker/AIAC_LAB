def grade(score):
    grade_mapping = {
        (90, 100): "A",
        (80, 89): "B",
        (70, 79): "C",
        (60, 69): "D",
        (0, 59): "F"
    }
    for (low, high), grade_letter in grade_mapping.items():
        if low <= score <= high:
            return grade_letter