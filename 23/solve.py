import datetime

fNumbers = [l.strip() for l in open("input-fnr.txt").readlines()]
ctrlNumbers1 = [3, 7, 6, 1, 8, 9, 4, 5, 2]
ctrlNumbers2 = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
date_format = '%d%m%y'


def isValidFNumber(fNumber):

    dateOfBirth = fNumber[0:6]
    try:
        date_obj = datetime.datetime.strptime(dateOfBirth, date_format)
    except ValueError:
        return False

    n = [int(num) for num in fNumber[0:9]]
    ctrlSum = sum([ctrlNumbers1[i]*n[i] for i in range(len(n))]) % 11
    if(ctrlSum == 0):
        n.append(0)
    elif(ctrlSum == 1):
        return False
    else:
        n.append(11-ctrlSum)

    ctrlSum = sum([ctrlNumbers2[i]*n[i] for i in range(len(n))]) % 11
    if(ctrlSum == 0):
        n.append(0)
    elif(ctrlSum == 1):
        return False
    else:
        n.append(11-ctrlSum)

    return fNumber == "".join([str(i) for i in n])


def isAugustWoman(fNumber):
    return fNumber[2:4] == "08" and int(fNumber[8:9]) % 2 == 0


s = 0
for fnum in fNumbers:
    if(isAugustWoman(fnum) and isValidFNumber(fnum)):
        s += 1

print(s)
