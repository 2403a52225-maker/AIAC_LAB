def analyze_csv_file(file_path):
    """
    Reads a .csv file and returns:
    - Total number of rows
    - Number of empty rows
    - Total number of words across the file

    Args:
        file_path (str): Path to the .csv file.

    Returns:
        tuple: (total_rows, empty_rows, total_words)
    """
    total_rows = 0
    empty_rows = 0
    total_words = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            total_rows += 1
            stripped_line = line.strip()
            if not stripped_line:
                empty_rows += 1
                continue
            # Split by comma, then count words in each cell
            cells = stripped_line.split(',')
            for cell in cells:
                words = cell.strip().split()
                total_words += len(words)
    return total_rows, empty_rows, total_words

# Example usage:
file_stats = analyze_csv_file('task 4.csv')
print(file_stats)
