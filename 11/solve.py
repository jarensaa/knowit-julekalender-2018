note = open("input-crisscross.txt").readline().strip()
moves = [note[i:i+2] for i in range(0, len(note), 2)]
x, y = 0, 0
for move in moves:
    if(move[1] == "V"):
        x -= int(move[0])
    elif(move[1] == "H"):
        x += int(move[0])
    elif(move[1] == "F"):
        y += int(move[0])
    else:
        y -= int(move[0])

print("[{},{}]".format(x, y))
