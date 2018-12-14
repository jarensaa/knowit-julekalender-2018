input = open("input-bounding-crisscross.txt").readline().strip()

moves = [input[i:i+2] for i in range(0, len(input), 2)]
spots = set()
spots.add((0, 0))

minX, maxX, minY, maxY, x, y = 0, 0, 0, 0, 0, 0
for move in moves:
    if(move[1] == 'F'):
        for i in range(int(move[0])):
            y += 1
            spots.add((x, y))
        maxY = max(maxY, y)
    elif(move[1] == 'V'):
        for i in range(int(move[0])):
            x -= 1
            spots.add((x, y))
        minX = min(minX, x)
    elif(move[1] == 'H'):
        for i in range(int(move[0])):
            x += 1
            spots.add((x, y))
        maxX = max(maxX, x)
    elif(move[1] == 'B'):
        for i in range(int(move[0])):
            y -= 1
            spots.add((x, y))
        minY = min(minY, y)


width = maxX - minX + 1
height = maxY - minY + 1

squareSize = width * height
visitedSpots = len(spots)
output = float(visitedSpots) / float(squareSize - visitedSpots)
print(output)
