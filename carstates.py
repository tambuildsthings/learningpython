command = ""
carStarted = False

while True:
    command = input(">> ").lower()
    if command == "start":
        if carStarted:
            print("Car is already started.")
        else:
            carStarted = True
            print("Car has started")
    elif command == "stop":
        if not carStarted:
            print("Car is already stopped.")
        else:
            carStarted = False
            print("Car has stopped")
    elif command == "help":
        print(
            """
start = start car
stop = stop car
quit = quit car command
"""
        )
    elif command == "quit":
        break
    else:
        print("I don't understand the command")
