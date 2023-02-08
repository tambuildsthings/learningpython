def is_armstrong_number(number):
    pwr = len(str(number))
    tot = 0
    for num in str(number):
        tot += int(num) ** pwr
    return tot == number


print(is_armstrong_number(153))
