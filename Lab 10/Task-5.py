import time
numbers = range(1, 1000000)
squared_numbers_loop = []
start_time = time.time()
for num in numbers:
    squared_numbers_loop.append(num ** 2)
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
print(len(squared_numbers_loop))
