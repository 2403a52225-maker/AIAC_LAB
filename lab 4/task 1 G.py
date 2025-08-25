import re

def is_valid_indian_mobile(number: str) -> bool:
    """
    Checks if the given string is a valid Indian mobile number.
    It must start with 6, 7, 8, or 9 and contain exactly 10 digits.
    """
    return bool(re.fullmatch(r'[6-9]\d{9}', number))
print(is_valid_indian_mobile("9876543210"))