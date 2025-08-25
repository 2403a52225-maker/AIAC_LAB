def extract_student_info(students):
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
    students = {
        "student1": {"full_name": "Alice Smith", "branch": "CSE", "SGPA": 8.5, "age": 20},
        "student2": {"full_name": "Bob Johnson", "branch": "ECE", "SGPA": 7.8, "age": 21},
    }
    print(extract_student_info(students))