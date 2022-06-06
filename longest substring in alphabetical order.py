# Print the longest substring of s in which the letters occur in alphabetical order.
# In the case of ties, print the first substring.

# Tricky s strings to solve for:
# "zyxwvutsrqponmlkjihgfedcba" should = z
# "rcizzyrtlmclvh" should = cizz
# "onuzgpnjhihvoxdgtjtvagw" should = nuz

s = "abcaohfacegiknop"
longestString = s[0]
testString = ""
count = 1

for letter in s:
    if testString == "":
        testString = letter
    print("comparing: " + letter + " with " + s[count : count + 1])
    if letter <= s[count : count + 1]:
        testString = testString + s[count]
        print("string so far is: " + testString)
    else:
        testString = ""
    if len(testString) > len(longestString):
        longestString = testString
        print("WIN!! " + longestString)
    count += 1
print("Longest substring in alphabetical order is: " + longestString)
