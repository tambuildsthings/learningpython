## Hangman game
#
## Requirements
# Here are the requirements for your game:
#
# The computer must select a word at random from the list of available words
# that was provided in words.txt.
# The functions for loading the word list and selecting a random word have
# already been provided for you in ps3_hangman.py.
#
# The game must be interactive; the flow of the game should go as follows:
#
# At the start of the game, let the user know how many letters the computer's
# word contains.
#
# Ask the user to supply one guess (i.e. letter) per round.
#
# The user should receive feedback immediately after each guess about whether
# their guess appears in the computer's word.
#
# After each round, you should also display to the user the partially guessed word
# so far, as well as letters that the user has not yet guessed.
#
## Some additional rules of the game:
# A user is allowed 8 guesses.
# Make sure to remind the user of how many guesses s/he has left after each round.
# Assume that players will only ever submit one character at a time (A-Z).

# A user loses a guess only when s/he guesses incorrectly.

# If the user guesses the same letter twice, do not take away a guess - instead,
# print a message letting them know they've already guessed that letter and ask
# them to try again.

# The game should end when the user constructs the full word or runs out of guesses.
# If the player runs out of guesses (s/he "loses"), reveal the word to the user
# when the game ends.

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

from ntpath import join
import random
import string

from numpy import append

WORDLIST_FILENAME = "/Users/tam/Documents/learningpython/scratch/words.txt"


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


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    
    For loop version:
    """
    # for letter in secretWord:
    #    if letter not in lettersGuessed:
    #        return False
    # return True
    """
    1 liner listcomp version:
    """
    return all(letters in lettersGuessed for letters in secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    
    For loop version:
    """
    # guessSummary = []
    # for letter in secretWord:
    #    if letter in lettersGuessed:
    #        guessSummary += " " + letter + " "
    #    else:
    #        guessSummary += " _ "
    # return guessSummary
    """
    1 liner list comp version:

    for each letter in secretWord,
    if that letter is in lettersGuessed,
    join that letter to the string,
    otherwise join an underscore.
    """
    return "".join(
        [
            str(" " + letter + " ") if letter in lettersGuessed else "".join(str(" _ "))
            for letter in secretWord
        ]
    )


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    # availableLetters = "abcdefghijklmnopqrstuvwxyz"
    # for letter in lettersGuessed:
    #    if letter in string.ascii_lowercase:
    #        availableLetters = availableLetters.replace(letter, "")
    # return availableLetters

    """
    1 liner list comp version:

    for each letter in the ascii alphabet,
    if that letter is in lettersGuessed,
    join a blank to the string,
    otherwise join the letter.
    """
    return "".join(
        [
            str("") if letter in lettersGuessed else "".join(str(letter))
            for letter in string.ascii_lowercase
        ]
    )


def hangman(secretWord):
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
    guessesRemaining = 8
    gameOver = False
    guessCommand = ""
    lettersGuessed = []

    print(
        "Welcome to the game Hangman!\nI am thinking of a word that is "
        + str(len(secretWord))
        + " letters long"
    )

    while gameOver == False:
        print("-----------")
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations, you won!")
            gameOver = True
        elif guessesRemaining > 0:
            print("You have " + str(guessesRemaining) + " guesses left")
            print("Available Letters: " + getAvailableLetters(lettersGuessed))
            guessCommand = input("Please guess a letter: ").lower()
            if len(guessCommand) == 1 and guessCommand in string.ascii_lowercase:
                if guessCommand in lettersGuessed:
                    print(
                        "Oops! You've already guessed that letter: "
                        + str(getGuessedWord(secretWord, lettersGuessed))
                    )
                elif guessCommand in secretWord:
                    lettersGuessed.append(guessCommand)
                    print(
                        "Good guess: " + str(getGuessedWord(secretWord, lettersGuessed))
                    )
                else:
                    lettersGuessed.append(guessCommand)
                    guessesRemaining -= 1
                    print(
                        "Oops! That letter is not in my word: "
                        + str(getGuessedWord(secretWord, lettersGuessed))
                    )
            elif guessCommand == "exit":
                print("Game over bro. The word was " + secretWord)
                gameOver = True
            else:
                print("Try again. Guess a single letter please.")
        else:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            gameOver = True


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
# secretWord = "spark"
hangman(secretWord)

