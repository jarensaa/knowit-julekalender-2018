counter = 0
goalNumber = 42
inputNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]
operands = [0]*(len(inputNumbers)-1)


def performOperations(inputNumbers, operands):
    copiedInput = list(inputNumbers)
    copiedOperands = list(operands)
    removed = 0
    global counter

    for i in range(0, len(operands)):
        p = i - removed
        operand = copiedOperands[p]

        if(operand == 2):
            removed += 1
            copiedInput[p+1] = int(str(copiedInput[p]) + str(copiedInput[p+1]))
            del copiedOperands[p]
            del copiedInput[p]

    totalSum = copiedInput[0]

    for i in range(1, len(copiedInput)):
        operand = copiedOperands[i - 1]
        if(operand == 0):
            totalSum += copiedInput[i]
        if(operand == 1):
            totalSum -= copiedInput[i]

    if (totalSum == goalNumber):
        counter += 1


def incementOperands(operands):
    for i in range(0, len(operands)):
        if(operands[i] < 2):
            operands[i] += 1
            return True

        if(i == (len(operands) - 1)):
            return False

        operands[i] = 0


incCounter = 0

while(incementOperands(operands)):
    if(incCounter % 10000 == 0):
        print("At " + str(incCounter) + "/" + str(3**14))
    performOperations(inputNumbers, operands)
    incCounter+= 1


print(counter)
