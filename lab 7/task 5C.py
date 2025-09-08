def greet_user(name, gender):
    gender = gender.lower()
    if gender == "male":
        title = "Mr."
    elif gender == "female":
        title = "Ms."
    else:
        title = "Mx."
    return f"Hello {title} {name}! Welcome."

if __name__ == "__main__":
    name = input("Enter your name: ").strip()
    gender = input("Enter your gender (Male/Female/Other): ").strip()
    print(greet_user(name, gender))