def sort_descending(int_list):
    """
    Takes a list of integers and returns the list sorted in descending order.

    Parameters:
    int_list (list): List of integers to sort.

    Returns:
    list: Sorted list in descending order.
    """
    return sorted(int_list, reverse=True)
print(sort_descending([1, 2, 3, 4, 5]))