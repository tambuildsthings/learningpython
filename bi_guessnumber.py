guessnum = 0
command = ""
highband = 100
lowband = 0
winner = False

print("Please think of a number between 0 and 100!")
while winner == False:
    guessnum = ((highband - lowband) // 2) + lowband
    print("Is your secret number " + str(guessnum))
    command = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
    )
    if command == "h":
        highband = guessnum
    elif command == "l":
        lowband = guessnum
    elif command == "c":
        print("Game over. Your secret number was: " + str(guessnum))
        winner = True
    else:
        print(">>I didn't understand. Please use h or l or c to communicate with me.")

