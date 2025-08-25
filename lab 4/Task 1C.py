def is_valid_indian_mobile(number):
    """
    Checks if the given number is a valid Indian mobile number.
    A valid Indian mobile number:
    - Starts with 6, 7, 8, or 9
    - Has exactly 10 digits
    """
    if isinstance(number, str) and number.isdigit() and len(number) == 10:
        return number[0] in {'6', '7', '8', '9'}
    return False
print(is_valid_indian_mobile("9876543210"))