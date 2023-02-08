"""
def getSublists(L, n):
    outputList = []
    start = 0
    while n <= len(L):
        outputList.append(L[start:n])
        n += 1
        start += 1
    print(outputList)
    return outputList


L = [1, 1, 1, 1, 4]
n = 2

getSublists(L, n)
"""


def dict_invert(d):
    """
    d: dict
    Returns an inverted dictionary according to the instructions above

    If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
    If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
    If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
    """
    newdic = {}
    for key in d:
        # print(key)
        # print(d[key])
        if d[key] not in newdic:
            newdic.update({d[key]: [key]})
        elif d[key] in newdic:
            newdic[d[key]].append(key)
            newdic[d[key]].sort()
    print(newdic)


d = {4: True, 2: True, 0: True}
dict_invert(d)

