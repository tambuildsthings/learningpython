numdic = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}
command = str(input("Digits to English converter. How can I help? "))
output = ""
# digits = len(command)
# i = 0
# while i < digits:
#    output += numdic[command[i]] + " "
#    i += 1

for no in command:
    output += numdic.get(no, "x") + " "
print(output)


def emojiConvert(message):
    words = message.split(" ")
    emojis = {":)": "🙂", ":(": "😞", ":0": "😮", ":P": "😛"}

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emojiConvert(message=input("Give me an emoji: > ")))
