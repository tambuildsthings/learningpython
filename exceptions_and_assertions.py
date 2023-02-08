# def fancy_divide(numbers, index):
#     try:
#         try:
#             denom = numbers[index]
#             for i in range(len(numbers)):
#                 numbers[i] /= denom
#         except IndexError:
#             fancy_divide(numbers, len(numbers) - 1)
#         else:
#             print("1")
#         finally:
#             print("0")
#     except ZeroDivisionError:
#         print("-2")


# def fancy_divide(list_of_numbers, index):
#     denom = list_of_numbers[index]
#     print([simple_divide(item, denom) for item in list_of_numbers])
#     return [simple_divide(item, denom) for item in list_of_numbers]


# def simple_divide(item, denom):
#     try:
#         return item / denom
#     except ZeroDivisionError:
#         return 0


# fancy_divide([0, 2, 4], 0)


def normalize(numbers):
    max_number = max(numbers)
    # check that max_number is not 0. If it is 0, stop and print the error
    assert max_number != 0, "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
        # check that the value for numbers[i] is more than 0 and less than 1. If not stop and print the error
        assert 0.0 <= numbers[i] <= 1.0, "output not between 0 and 1"
    return numbers


normalize([0, 0, 0])
