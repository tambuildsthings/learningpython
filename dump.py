"""
s = "plabcdplplpljklmplplpl"  # "plabcdplplpljklmnopqplplpl" "plabcdefplplpljklmplplpl" "plabcdplplpljklmplplpl"
alphabet = "abcdefghijklmnopqrstuvwxyz"
longestString = ""
testString = ""
letterIndex = -1

for letter in s:
    print("checking: " + letter)
    testString = letter
    letterIndex += 1
    # get the index of this letter in the alphabet
    alphabetIndex = alphabet.index(letter)
    # if letterIndex +addon == alphabetIndex +addon
    addon = 1
    while s[letterIndex + addon] == alphabet[alphabetIndex + addon]:
        # print("We're on to something")
        # print(s[letterIndex] + s[letterIndex + addon])
        testString = testString + s[letterIndex + addon]
        # print("longest test string is: " + testString)
        addon += 1
        # print("addon is now: " + str(addon))
        if len(testString) > len(longestString):
            longestString = testString
            print("WINNER! Longest string is: " + str(longestString))

print("Longest substring in alphabetical order is: " + str(longestString))


#### Attempt 2

alphabet = "abcdefghijklmnopqrstuvwxyz"
longestString = ""
testString = ""
letterIndex = -1
addon = 1

for letter in s:
    print("letter is: " + letter)
    letterIndex += 1
    alphabetIndex = alphabet.index(letter)
    print(
        "comparing: "
        + s[letterIndex : letterIndex + addon]
        + " with "
        + alphabet[alphabetIndex : alphabetIndex + addon]
    )
    while (
        s[letterIndex : letterIndex + addon]
        == alphabet[alphabetIndex : alphabetIndex + addon]
    ):
        testString = s[letterIndex : letterIndex + addon]
        print("testString: " + testString)
        addon += 1
    if len(testString) > len(longestString):
        longestString = testString

print("Longest substring in alphabetical order is: " + str(longestString))

#### Attempt 3

longestString = ""
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

if len(longestString) > 1:
    print("Longest substring in alphabetical order is: " + longestString)
else:
    print("Longest substring in alphabetical order is: " + s[0])
"""
s = 1
while s <= 26:
    print(s)
    s += 1
