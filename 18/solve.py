from pprint import pprint
from operator import add

actions = list(open("input-rpslog.txt").readline().strip())


def getUniqueCharsInString(string):
    unique = []
    for char in string[::]:
        if char not in unique:
            unique.append(char)
    return len(unique)


def isDraw(inputActionsString):
    uniqueHands = getUniqueCharsInString(inputActionsString)
    if(uniqueHands == 1 or uniqueHands == 3):
        return True
    return False


def hasSpecificWinner(string):
    sortedString = ''.join(sorted(string))
    return (sortedString == "PPS" or sortedString == "PRR" or sortedString == "RSS")


def getSpecificWinner(string):
    returnTupple = []
    for char in string:
        if(string.count(char) == 1):
            returnTupple.append(1)
        else:
            returnTupple.append(0)

    return tuple(returnTupple)


def getTwoManWinner(actionsInput, loser):

    action = actionsInput.pop(0) + actionsInput.pop(0)

    if(isDraw(action)):
        return getTwoManWinner(actionsInput, loser)

    if(action == "RS"):
        winner = [1, 0]
    elif(action == "SP"):
        winner = [1, 0]
    elif(action == "PR"):
        winner = [1, 0]
    elif(action == "SR"):
        winner = [0, 1]
    elif(action == "PS"):
        winner = [0, 1]
    elif(action == "RP"):
        winner = [0, 1]

    returnTupple = []
    for i in loser:
        if(i == 0):
            returnTupple.append(winner.pop(0))
        else:
            returnTupple.append(0)

    return tuple(returnTupple)


def getLoser(string):
    returnTupple = []
    for char in string:
        if(string.count(char) == 1):
            returnTupple.append(1)
        else:
            returnTupple.append(0)

    return tuple(returnTupple)


def getWinner(actionsInput):
    action = actionsInput.pop(0) + actionsInput.pop(0) + actionsInput.pop(0)
    if(isDraw(action)):
        return getWinner(actionsInput)

    if(hasSpecificWinner(action)):
        return getSpecificWinner(action)

    return getTwoManWinner(actionsInput, getLoser(action))


scores = (0, 0, 0)
while(len(actions) > 2):
    players = 3
    winner = getWinner(actions)
    scores = tuple(map(add, scores, winner))

print(str(scores).strip("(").strip(")").replace(" ", ""))
