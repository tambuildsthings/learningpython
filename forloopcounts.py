from this import d


for item in [1, 2, 3, 4, 5]:
    print(item)

for lots in range(20, 40, 5):
    print(lots)

prices = [10, 20, 30]
total = 0
for items in prices:
    total += items
print(f"Total shopping: £{total}")

# nested loops
for x in range(4):
    for y in range(3):
        print(f"{x}, {y}")

# draw an F
numbers = [5, 2, 5, 2, 2]
for nos in numbers:
    output = ""
    for xs in range(nos):
        output += "x"
    print(output)

names = ["John", "Bob", "Tam", "Sarah", "Mary"]
names[2] = "Tammy"
print(names[2:4])

numbers = [2, 7, 4, 13, 5, 18, 1]
highest_number = 0
for nums in numbers:
    if nums > highest_number:
        highest_number = nums
print(highest_number)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1][2] = "six"

for row in matrix:
    for item in row:
        print(item)
