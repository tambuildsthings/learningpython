## Wordle clone
# -----------------------------------

import random

WORDLIST_FILENAME = "/Users/tam/Documents/learningpython/scratch/wordlewords.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, wordsGuesedLatest):
    """
    secretWord: string, the word the user is guessing
    wordsGuessedLatest: string, newest guess from input
    returns: boolean, True if secretWord is the latest guessed word (so you win);
      False otherwise
    """
    return secretWord == wordsGuesedLatest


def checkWord(secretWord, wordsGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    wordsGuessed: list, what words have been guessed so far
    returns: string with the guessed word followed by a result made up of 
    lower case letters for letters in the secretWord but not in the right place
    upper case letters for letters in the secretWord AND in the right place
    underscores which show letters not the in the secretWord.
    
    """
    wordResult = wordsGuessed[-1]
    indexCounter = 0
    for letter in wordsGuessed[-1]:
        if (
            letter in secretWord
            and wordsGuessed[-1][indexCounter] == secretWord[indexCounter]
        ):
            wordResult += " " + letter.upper() + " "
        elif (
            letter in secretWord
            and wordsGuessed[-1][indexCounter] != secretWord[indexCounter]
        ):
            wordResult += " " + letter.lower() + " "
        else:
            wordResult += " _ "
        indexCounter += 1
    return wordResult


def getResults(results):
    for r in results:
        print(r)


def getAvailableLetters(wordsGuessed):
    """
    wordsGuessed: list, what words have been guessed so far
    returns: string, the letters that have not yet been guessed.
    """
    uniqueLetters = ""
    availableLetters = "abcdefghijklmnopqrstuvwxyz"
    for words in wordsGuessed:
        for letter in words:
            if letter not in uniqueLetters:
                uniqueLetters += letter
                availableLetters = availableLetters.replace(letter, "")
    return availableLetters


def wordle(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    guessesRemaining = 6
    gameOver = False
    guessCommand = ""
    wordsGuessed = []
    results = []

    print(
        "\n~~~~Let's play Wordle!~~~~\nI am thinking of a word that is 5 letters long. Guess 5 letter words please."
    )

    while gameOver == False:
        print("-----------")
        if isWordGuessed(secretWord, guessCommand) == True:
            print("!!! Congratulations, you won!")
            gameOver = True
        elif guessesRemaining > 0:
            print("Guesses left: " + str(guessesRemaining))
            guessCommand = input("Please guess a 5 letter word: ").lower()
            if len(guessCommand) == 5:
                if guessCommand in wordsGuessed:
                    print("Oops! You've already guessed that word.")
                    getResults(results)
                # elif guessCommand not in wordlist:
                # print("Invalid word.")
                else:
                    guessesRemaining -= 1
                    wordsGuessed.append(guessCommand)
                    results.append(checkWord(secretWord, wordsGuessed))
                    getResults(results)
                    print("Unused letters: " + getAvailableLetters(wordsGuessed))
            elif guessCommand == "exit":
                print("Thanks for playing. Your word was " + secretWord)
                gameOver = True
            else:
                print("Try again. Guess a 5 letter word please.")
        else:
            print("Game over! You ran out of guesses. The word was: " + secretWord)
            gameOver = True


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
# secretWord = "kayak"
# words to check "cabBy" "fleEt" "kayaK" "babes"
wordle(secretWord)

