def calculate_power_bill(units):
    """
    Calculate the power bill based on the number of units consumed.
    The rates are as follows:
        - For first 100 units: $0.5 per unit
        - For next 100 units (101-200): $0.75 per unit
        - For next 100 units (201-300): $1.20 per unit
        - Above 300 units: $1.50 per unit
    A fixed charge of $50 is added to every bill.

    Parameters:
    units (float): Number of units consumed.

    Returns:
    float: Total power bill amount.
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")

    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 300:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10 # Fixed charge
    return bill

# Example usage:
if __name__ == "__main__":
    try:
        units = float(input("Enter the number of units consumed: "))
        total_bill = calculate_power_bill(units)
        print(f"Total power bill: {total_bill:.2f}")
    except ValueError as e:
        print(e)
print(calculate_power_bill(100))
