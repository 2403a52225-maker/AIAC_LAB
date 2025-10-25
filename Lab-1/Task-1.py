def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Example usage:
input_str = "A man, a plan, a canal: Panama"
print(is_palindrome(input_str))  # Output: True
