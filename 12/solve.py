import binascii

emojis = list(open("input.txt").readline())
unicodeTail = ""
output = ''.join([chr(int(str(str.encode(emoji))[16:18], 16)-96)
                  for emoji in emojis])
print(output)
