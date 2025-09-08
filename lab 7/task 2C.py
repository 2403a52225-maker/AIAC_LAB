def loan_approval():
    print("Loan Approval System")
    name = input("Enter your name: ").strip()
    gender = input("Enter your gender (Male/Female/Other): ").strip()
    try:
        income = float(input("Enter your annual income (in USD): ").strip())
    except ValueError:
        print("Invalid income input. Setting to 0.")
        income = 0.0
    try:
        credit_score = int(input("Enter your credit score (300-850): ").strip())
    except ValueError:
        print("Invalid credit score input. Setting to 300.")
        credit_score = 300

    # AI-generated logic (simulate possible bias for demonstration)
    # This logic should NOT be used in production; it's for bias evaluation only.
    approved = False
    reason = ""

    # Example of potentially biased logic (for evaluation purposes)
    if name.lower() in ["john", "michael", "david"]:
        # Lower threshold for these names
        if income >= 30000 and credit_score >= 600:
            approved = True
        else:
            reason = "Income or credit score too low."
    elif name.lower() in ["priya", "ananya", "fatima"]:
        # Higher threshold for these names
        if income >= 40000 and credit_score >= 700:
            approved = True
        else:
            reason = "Income or credit score too low."
    else:
        # Default criteria
        if income >= 35000 and credit_score >= 650:
            approved = True
        else:
            reason = "Income or credit score too low."

    # Gender-based message (should not affect approval, but included for evaluation)
    if gender.lower() == "female":
        gender_msg = "Thank you for applying, Ma'am."
    elif gender.lower() == "male":
        gender_msg = "Thank you for applying, Sir."
    else:
        gender_msg = "Thank you for applying."

    print(gender_msg)
    if approved:
        print(f"Congratulations {name}, your loan is approved!")
    else:
        print(f"Sorry {name}, your loan is not approved. Reason: {reason}")

if __name__ == "__main__":
    loan_approval()
