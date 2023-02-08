def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """

    def helpLaceStrings(s1, s2, out):
        if s1 == "":
            # put the rest of s2 on the end of out
            return out + s2
        if s2 == "":
            # put the rest of s1 on the end of out
            return out + s1
        else:
            # remove the first letter from each string and make out string with those letters
            # then recur the function
            return helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2[0])

    return helpLaceStrings(s1, s2, "")


s1 = "ab"
s2 = "vwxy"

print(laceStringsRecur(s1, s2))
