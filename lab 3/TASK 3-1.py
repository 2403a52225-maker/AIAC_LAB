def calculate_power_bill(units, rate_per_unit):
    """
    Calculate the total power bill.

    Parameters:
    units (float): Number of units consumed.
    rate_per_unit (float): Cost per unit.

    Returns:
    float: Total bill amount.
    """
    return units * rate_per_unit

def main():
    try:
        units = float(input("Enter the number of units consumed: "))
        rate = float(input("Enter the rate per unit: "))
        total_bill = calculate_power_bill(units, rate)
        print(f"Total power bill: ${total_bill:.2f}")
    except ValueError:
        print("Please enter valid numbers for units and rate.")

if __name__ == "__main__":
    main()
