def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(len(lines))
    except FileNotFoundError:
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Static file path
file_path = "EXAMPLE.txt.txt" 


# Call the function and print the result
line_count = count_lines_in_file(file_path)
print(f"The file '{file_path}' has {line_count} lines.")