f = open("numbers.txt","r")
nums = f.readlines()

squares = []
for num in nums:
    num_str = num.strip()
    if num_str.isdigit():
        n = int(num_str)
        squares.append(n * n)

f2 = open("squares.txt","w")
for sq in squares:
    f2.write(str(sq) + "\n")

print("Squares written")