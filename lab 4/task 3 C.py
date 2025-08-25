def extract_student_info(students):
    """
    Extracts 'full_name', 'branch', and 'SGPA' for each student from the nested dictionary.

    Args:
        students (dict): Nested dictionary of student information.

    Returns:
        list: List of dictionaries with keys 'full_name', 'branch', and 'SGPA'.
    """
    result = []
    for student in students.values():
        info = {
            "full_name": student.get("full_name"),
            "branch": student.get("branch"),
            "SGPA": student.get("SGPA")
        }
        result.append(info)
    return result

# Example usage:
if __name__ == "__main__":
    students1 = {
        "student1": {"full_name": "Alice Smith", "branch": "CSE", "SGPA": 8.5, "age": 20},
        "student2": {"full_name": "Bob Johnson", "branch": "ECE", "SGPA": 7.8, "age": 21},
    }
    print(extract_student_info(students1))
    students2 = {
        "student1": {"full_name": "John Doe", "branch": "ME", "SGPA": 9.0},
        "student2": {"full_name": "Jane Roe", "branch": "CSE", "SGPA": 8.7},
        "student3": {"full_name": "Mike Lee", "branch": "EE", "SGPA": 8.0},
    }
    print(extract_student_info(students2))
