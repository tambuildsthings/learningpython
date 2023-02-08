def square_of_sum(number):
    numSum = 0
    for num in range(1, number + 1):
        numSum += num
    return numSum ** 2


def sum_of_squares(number):
    squaresSum = 0
    for num in range(1, number + 1):
        squaresSum += num ** 2
    return squaresSum


def difference_of_squares(number):
    print(square_of_sum(number) - sum_of_squares(number))
    return square_of_sum(number) - sum_of_squares(number)


difference_of_squares(10)

