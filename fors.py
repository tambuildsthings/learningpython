for nums in range(2, 11, 2):
    print(nums)
print("Goodbye!")

print("Hello!")
for nums in range(10, 0, -2):
    print(nums)

end = 6
total = 0
for nums in range(0, end + 1):
    total += nums
print(total)

count = 0
for letter in "Snow!":
    print("Letter # " + str(count) + " is " + str(letter))
    count += 1
    break
print(count)

divisor = 2
for num in range(0, 10, 2):
    print(num / divisor)

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print("Foo!")
