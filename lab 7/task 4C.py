def score_applicant(education, experience, gender, age):
    """
    Scores a job applicant based on education, experience, gender, and age.
    Returns a score out of 100.
    """
    score = 0

    # Education scoring
    education_levels = {
        "none": 0,
        "highschool": 10,
        "associate": 20,
        "bachelor": 30,
        "master": 40,
        "phd": 50
    }
    score += education_levels.get(education.lower(), 0)

    # Experience scoring (years)
    if experience < 0:
        experience_points = 0
    elif experience < 2:
        experience_points = 5
    elif experience < 5:
        experience_points = 15
    elif experience < 10:
        experience_points = 25
    else:
        experience_points = 35
    score += experience_points

    # Gender scoring (no bias, all genders treated equally)
    if gender.lower() in ["male", "female", "other"]:
        gender_points = 5
    else:
        gender_points = 0
    score += gender_points

    # Age scoring (prefer working age: 22-60)
    if 22 <= age <= 60:
        age_points = 10
    elif 18 <= age < 22 or 61 <= age <= 70:
        age_points = 5
    else:
        age_points = 0
    score += age_points

    # Cap score at 100
    return min(score, 100)

def main():
    print("Job Applicant Scoring System")
    education = input("Enter education level (None, Highschool, Associate, Bachelor, Master, PhD): ").strip()
    try:
        experience = int(input("Enter years of experience: ").strip())
    except ValueError:
        print("Invalid experience input. Setting to 0.")
        experience = 0
    gender = input("Enter gender (Male, Female, Other): ").strip()
    try:
        age = int(input("Enter age: ").strip())
    except ValueError:
        print("Invalid age input. Setting to 0.")
        age = 0

    score = score_applicant(education, experience, gender, age)
    print(f"Applicant Score: {score}/100")

if __name__ == "__main__":
    main()
