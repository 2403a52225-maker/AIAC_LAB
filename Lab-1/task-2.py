def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Taking user input
terms = int(input("Enter the number of terms: "))

# Check for valid input
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci sequence up to {terms} terms:")
    print(fibonacci(terms))
