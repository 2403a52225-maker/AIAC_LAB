def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

try:
    n = int(input("Enter the value of n to compute the nth Fibonacci number: "))
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
except ValueError:
    print("Please enter a valid integer.")
