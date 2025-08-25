def most_frequent_word(text):
    import string
    from collections import Counter

    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split into words
    words = text.split()
    # Count word frequencies
    counts = Counter(words)
    # Return the most common word
    return counts.most_common(1)[0][0]

# Example usage:
if __name__ == "__main__":
    print(most_frequent_word("Hello, hello! How are you?"))  # Output: "hello"
    print(most_frequent_word("The quick brown fox jumps over the lazy dog. The dog was not amused."))  # Output: "the"
    print(most_frequent_word("Apples and oranges, apples are great. Oranges are fine too!"))  # Output: "apples"
