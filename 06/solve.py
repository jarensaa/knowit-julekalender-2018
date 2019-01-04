import math

def isNullTungt(number):
  numberList = list(str(number))
  count = 0

  for character in numberList:
    if(character == "0"):
      count += 1
  
  if(count > (len(numberList)/2)):
    return True
  
  return False


sum = 0
for number in range(0,18163106):
  if(isNullTungt(number)):
     sum += number
  if(number % 100000 == 0):
     print("{:8d}/18163106".format(number))

  

print(sum)