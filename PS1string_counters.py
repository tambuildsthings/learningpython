# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

s = "ekjrhgleitugpirtkbnelfkjgvleih"
count = 0

for letter in s:
    if (
        letter == "a"
        or letter == "e"
        or letter == "i"
        or letter == "o"
        or letter == "u"
    ):
        count += 1

print("Number of vowels: " + str(count))

# Write a program that prints the number of times the string 'bob' occurs in s.

bobcount = 0
index = -1
isbob = ""
s = "abzcbobobegghabobkl"

for letter in s:
    # get the index of the current letter
    index += 1
    # is letter "b"
    if letter == "b":
        # look forwards 3 letters and save those 3 letters as isbob var
        isbob = s[index : index + 3]
        if isbob == "bob":
            bobcount += 1

print("Number of times bob occurs is: " + str(bobcount))

# Print the longest substring of s in which the letters occur in alphabetical order.
# In the case of ties, print the first substring.
s = "rcizzyrtlmclvh"  # "plabcdplplpljklmnopqplplpl"
# "plabcdefplplpljklmplplpl" "plabcdplplpljklmplplpl" "rvabcdplhijklmpl"
# "abcaohfacegiknop"
# Tricky ones:
# "zyxwvutsrqponmlkjihgfedcba" = z
# "rcizzyrtlmclvh" = cizz
# "onuzgpnjhihvoxdgtjtvagw" = nuz

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
