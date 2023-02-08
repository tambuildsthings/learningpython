def score(word):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter = 0
    scoresList = []
    for letter in word.lower():
        scoresList.append((alphabet.index(letter) + 1) * counter)
        counter += 1
    scoresList.sort()
    h1 = scoresList[-1]
    h2 = scoresList[-2]
    return f(h1, h2)


def f(h1, h2):
    return h1 + h2


word = "BALLBAG"
print(score(word))
