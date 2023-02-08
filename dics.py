"""
customer = {"name": "Tam Finlay", "age": 33, "isVerified": True}

print(customer["age"])
print(customer.get("age"))
print(customer.get("location", "earth"))  # not sure what the point in this is
print(customer)
customer["name"] = "Thomas Finlay"
print(customer)
customer["birthdate"] = "1st Nov 1987"
print(customer)

numdic = {"1": "one", "2": "two", "3": "three", "4": "four"}
command = str(input("Digits to English converter. How can I help? "))

digits = len(command)
print(digits)

i = 0
output = ""
while i < digits:
    output += numdic[command[i]]
    i += 1
print(output)
"""

animals = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati"]}
animals["d"] = ["donkey"]
animals["d"].append("dog")
animals["d"].append("dingo")


def how_many(aDict):
    tot = 0
    for key in aDict:
        for element in aDict[key]:
            tot += 1
    print(tot)
    return tot


# how_many(animals)


emptyDs = {"u": []}
midDs = {"a": ["aardvark"], "b": ["baboon", "balls", "burp"], "c": ["coati"]}
longDs = {
    "a": [15, 2],
    "c": [18, 13, 10, 11, 10],
    "b": [7, 3, 14, 1, 18, 5, 13, 10, 2, 11],
    "d": [18],
}


def biggest(aDict):
    tempHighest = 0
    winner = []
    for key in aDict:
        if len(aDict) == 1:
            winner = key
        if len(aDict[key]) > tempHighest:
            tempHighest = len(aDict[key])
            winner = key
    return winner


print(biggest(emptyDs))
print(biggest(midDs))
print(biggest(longDs))

"""
TA's  1 liner solution:

def biggest(d):
    return sorted((len(v), k) for k, v in d.items())[-1][1]

sorted((len(v), k) for k, v in d.items()) returns a sorted list of tuples, 
each tuple containing the length of the keys values followed by the key itself. 

So the 3rd one gives: [(1, 'd'), (2, 'a'), (5, 'c'), (10, 'b')]

[-1] takes the one at the end which is (10, 'b')

[1] takes the 2nd element of the tuple which is 'b'
"""


def biggestTA(d):
    return sorted((len(v), k) for k, v in d.items())[-1][1]


print(biggestTA(emptyDs))
print(biggestTA(midDs))
print(biggestTA(longDs))
