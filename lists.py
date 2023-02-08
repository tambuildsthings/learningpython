numbers = [2, 14, 20, 4, 2, 8, 3, 12]
numbers.insert(2, 45)  # insert at position index, value
numbers.remove(2)  # remove this value once
numbers.pop()  # remove last value
numbers2 = numbers.copy()
numbers2.append(30)  # add value to end of list
words = ["bum", "pig"]

print(numbers)
print(numbers2)
print(words)
print(words[0])
print(words[-1])
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers.index(8))
print(8 in numbers)
print(numbers.count(8))

# remove duplicates. This doesn't work but not sure why
dupes = [5, 3, 2, 17, 17, 5, 2, 8, 5, 5, 1, 5]
print(dupes)
for nums in dupes:
    print(f"checking for {nums}")
    print(f"duplicates count is {dupes.count(nums)}")
    if dupes.count(nums) > 1:
        print(f"removing one instance of {nums}")
        dupes.remove(nums)
        print(f"the trimmed list is: {dupes}")
print(dupes)

# remove duplicates. This does work.
dupeSource = [5, 3, 2, 17, 17, 5, 2, 8, 5, 5, 1, 5]
dupeTrimmed = []
for nums in dupeSource:
    if nums not in dupeTrimmed:
        dupeTrimmed.append(nums)
print(dupeTrimmed)

# unpacking
biglistofbignumbers = [120, 439, 293, 257, 831]
a, b, c, d, e = biglistofbignumbers
print(b)

# walking up lists to make new lists
def getSublists(L, n):
    outputList = []
    start = 0
    while n <= len(L):
        outputList.append(L[start:n])
        n += 1
        start += 1
    print(outputList)
    return outputList


L = [1, 2, 1, 3, 4]
n = 3

getSublists(L, n)

## Sort a list with selection sort (good for numbers)
def selectionSort(L):
    suffixLen = 0
    while suffixLen != len(L):
        for i in range(suffixLen, len(L)):
            if L[i] < L[suffixLen]:
                L[suffixLen], L[i] = L[i], L[suffixLen]
        suffixLen += 1


## Sort a list with selection sort (good for numbers or letters)
def selectionSort2(L2):
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L2)):
            if L2[j - 1] > L2[j]:
                clear = False
                temp = L2[j]
                L2[j] = L2[j - 1]
                L2[j - 1] = temp


L = [2, 5, 7, 3, 8, 9, 4, 1, 6, 4, 13, 11]
print(L)
selectionSort(L)
print(L)

L2 = ["d", "m", "a", "k", "b", "l", "q", "e", "c"]
print(L2)
selectionSort2(L2)
print(L2)


def swapSort(L):
    """L is a list of integers or letters"""
    print("Original L: ", L)
    for i in range(len(L)):
        # use this one to order high to low:
        for j in range(len(L)):
            ## use this one to order low to high:
            # for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)


swapSort(L)
