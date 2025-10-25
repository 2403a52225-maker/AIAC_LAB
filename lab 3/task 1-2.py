def get_user_factorial():
    try:
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return None
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None
print(get_user_factorial())