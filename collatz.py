def steps(number):
    if type(number) == str:
        raise ValueError("Not strings please. Only positive integers are allowed")
    if number == 1:
        return 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    stepsTotal = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        stepsTotal += 1
    return stepsTotal


print(steps(12))
