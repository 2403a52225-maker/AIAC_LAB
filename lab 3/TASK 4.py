def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.

    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

def print_fahrenheit_for_celsius(celsius):
    """
    Print the Fahrenheit equivalent of a given Celsius temperature.

    Parameters:
    celsius (float): Temperature in Celsius.
    """
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
print(celsius_to_fahrenheit(0))