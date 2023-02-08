"""
We can use the idea of bisection search to determine if a character is in a string, 
so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for
 (the "test character"). 
 
If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" 
than the middle character. 
If so, we need only consider the lower half of the string; 

otherwise, we only consider the upper half of the string. 

Implement the function isIn(char, aStr) which implements the above idea recursively
 to test if char is in aStr. 
 char will be a single character and aStr will be a string that is in alphabetical order. 
 The function should return a boolean value.

"""


def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    """
    # if aStr is empty return false
    if aStr == "":
        # print("aStr is empty")
        return False
    # if aStr is 1 len 1 then check just that character
    if len(aStr) == 1:
        if char == aStr:
            # print("aStr is only 1 letter and it matches char")
            return True
        else:
            # print("aStr is only 1 letter and it is not char")
            return False
    # if middle character of aStr is char return true
    charIndex = len(aStr) // 2
    if aStr[charIndex] == char:
        # print("The middle letter of aStr is char")
        return True
    # otherwise figure out which side of aStr to look at again
    else:
        # print("charIndex is: " + str(charIndex) + ". (" + aStr[charIndex] + (")"))
        if char < aStr[charIndex]:
            lowerIndex = 0
            upperIndex = charIndex
            # print("Looking again lower")
            return isIn(char, aStr[lowerIndex:upperIndex])
        else:
            lowerIndex = charIndex
            upperIndex = len(aStr)
            # print("Looking again higher")
            return isIn(char, aStr[lowerIndex:upperIndex])


print(isIn("h", "behillppuwxxxz"))

# abcdefghijklmnop
