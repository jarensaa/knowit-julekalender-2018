def getCharValue(inputChar):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ".find(inputChar) + 1


inputString = "GODJULOGGODTNYTTÅR"
value = 0

for i in range(len(inputString)):
    charAtIndex = inputString[i]
    power = len(inputString) - i - 1
    value += (29**power)*getCharValue(charAtIndex)

print(value)
