currentYear = 2022
currentMonth = 5
currentDay = 22

name = input("What is your name please? ")
if len(name) < 3:
    print("You're name is very short mate.")
elif len(name) > 20:
    print("That is a very long name mate.")
else:
    print("Hi " + name)

favColour = input("So tell me, " + name + ", What's your favourite colour? ")
print("~~~~ BRRRR Robot knows " + name + "'s favourite colour is " + favColour.lower())

birthYear = int(input("What year were you born please? "))
birthMonth = input("What month were you born? (as a number please) ")
ageInYears = currentYear - birthYear

age = ageInYears
if int(birthMonth) > currentMonth:
    age = ageInYears - 1
if int(birthMonth) == currentMonth:
    birthDay = input("What day were you born? (as a number please) ")
    if int(birthDay) > currentDay:
        age = ageInYears - 1

formattedString = f"~~~~ Aaaarrrr Robot knows {name}'s age is {age}"
print(formattedString)

housePrice = 1000000
desireForHouse = input("Do you want to buy my house? It's £1 million. ")
if desireForHouse.lower() == "yes":
    goodCreditRating = input("Do you have a good credit rating? ")
    if goodCreditRating.upper() == "YES":
        houseDeposit = housePrice * 0.1
        print(f"I will need £{houseDeposit} deposit for a mortgage.")
    else:
        houseDeposit = housePrice * 0.2
        print(f"I will need £{houseDeposit} deposit for a mortgage.")
