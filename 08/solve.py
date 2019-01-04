file = open('input-dolls.txt')
dolls = []
count = 0

for line in file:
    print(line)
    doll = {}
    doll["height"] = int(line.split(",")[1])
    doll["color"] = line.split(",")[0]
    dolls.append(doll)


dolls = sorted(dolls, key=lambda k: k["height"])
outerDoll = dolls[0]

for doll in dolls:
    if(doll["color"] != outerDoll["color"] and doll["height"] > outerDoll["height"]):
        count += 1
        outerDoll = doll

print(count)
