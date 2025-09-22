def calculate_area_of_rectangle(length: float, breadth: float) -> float:
    """
    Calculate the area of a rectangle.

    Parameters:
        length (float): The length of the rectangle.
        breadth (float): The breadth of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * breadth

if __name__ == "__main__":
    rectangle_length = 10
    rectangle_breadth = 20
    area = calculate_area_of_rectangle(rectangle_length, rectangle_breadth)
    print(f"The area of the rectangle is: {area}")