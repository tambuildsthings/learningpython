balance = 320000
annualInterestRate = 0.2


"""
Monthly interest rate = (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

"""
PROBLEM 1
year = 12
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12

for months in range(year):
    #print("This is month: " + (str(months + 1)))
    balance = balance - (balance * monthlyPaymentRate)
    balance = balance + (balance * monthlyInterestRate)

print("Remaining balance: " + str(round(balance, 2)))
"""

"""
PROBLEM 2
year = 12
monthlyInterestRate = annualInterestRate / 12
guessPayment = 10
endOfYearBalance = balance

while endOfYearBalance > 0:
    for months in range(year):
        endOfYearBalance -= guessPayment
        endOfYearBalance += endOfYearBalance * monthlyInterestRate
        # print("Remaining balance: " + str(round(balance, 2)))
    if endOfYearBalance > 0:
        endOfYearBalance = balance
        guessPayment += 10
print("Lowest payment: " + str(guessPayment))
"""

monthlyInterestRate = annualInterestRate / 12
lowerBound = round(balance / 12, 2)
upperBound = round((balance * (1 + monthlyInterestRate) ** 12) / 12.0, 2)
guessPayment = ((upperBound - lowerBound) / 2) + lowerBound
endOfYearBalance = balance
year = 12

while endOfYearBalance != 0.00:
    for months in range(year):
        endOfYearBalance -= guessPayment
        endOfYearBalance += endOfYearBalance * monthlyInterestRate
    endOfYearBalance = round(endOfYearBalance, 2)
    if endOfYearBalance != 0.00:
        # update the bounds up or down
        if endOfYearBalance > 0:
            lowerBound = guessPayment
        else:
            upperBound = guessPayment
        # generate a new guess with the new bounds
        guessPayment = ((upperBound - lowerBound) / 2) + lowerBound
        # reset balance for the next loop
        endOfYearBalance = balance
print("Lowest payment: " + str(round(guessPayment, 2)))
