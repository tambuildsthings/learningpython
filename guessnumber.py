import math
import numpy
import matplotlib

secretNumber = 9
guessCount = 0
guessLimit = 3

print(math.sqrt(16))
print("Can you guess the secret number? It is 0 to 9. You have 3 guesses.")
while guessCount < guessLimit:
    guess = int(input("What's your guess? "))
    guessCount += 1
    if guess == secretNumber:
        print("Yes! You won!")
        break
    else:
        print("Try again.")
else:
    print("Sorry mate you lost the game.")
print("Thanks for playing.")
