import csv

def analyze_csv(file_path):
    total_rows = 0
    empty_rows = 0
    word_count = 0

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            # Check if all fields are empty or whitespace
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            # Count words in non-empty cells
            for cell in row:
                word_count += len(cell.strip().split())

    return total_rows, empty_rows, word_count

# Example usage:
total, empty, words = analyze_csv('task 4.csv')
print(f"Total Rows = {total}, Empty Rows = {empty}, Word Count = {words}")