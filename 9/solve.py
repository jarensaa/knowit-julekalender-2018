import hashlib
import json


def getHash(inputString):
    return hashlib.md5(inputString.encode('utf-8')).hexdigest()


data = json.loads(open("input-hashchain.json").read())
currentHash = getHash("julekalender")
outputString = ""

while(len(outputString) < len(data)):
    for hashedChar in data:
        newHash = getHash(currentHash + hashedChar['ch'])
        if(newHash == hashedChar['hash']):
            outputString += hashedChar['ch']
            currentHash = newHash


print(outputString)
