import random

people = ["Tam", "Bob", "Mary", "Wendy"]

for i in range(3):
    # random number between 0 and 1
    print(random.random())
    # random int between the two arguments inclusive
    print(random.randint(10, 20))
    # random item from a list
    print(random.choice(people))

# Roll two dice:
# class called Dice. A method called roll() with a tuple.


class Dice:
    def __init__(self, dices, sides) -> None:
        self.dices = dices
        self.sides = sides

    def roll(self):
        tempResults = []
        for i in range(self.dices):
            tempResults.append(random.randint(1, self.sides))
        results = tuple(tempResults)
        return results


rollDice = Dice(2, 6)
print(rollDice.roll())
