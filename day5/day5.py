from copy import deepcopy

with open("input.txt", "r") as file:
    input = file.read().split("\n")

vS = [] # vS
cS = [] # cS
moves = []
space_count = 0

for line in input:
    if line.startswith("m"):
        filtered = line.replace("move ", "").replace("from ","").replace("to ","")
        filtered = filtered.split(" ")
        moves.append([filtered[0],filtered[1],filtered[2]])
    elif line.startswith(" 1"):
        for i in range(int(line[len(line)-1])):
            cS.append([])
        for i in range(input.index(line)):
            vS.append([])
        for line in input[0:input.index(line)]:
            for i in range(len(line)):
                if line[i] == " ":
                    space_count += 1
                    if space_count == 4:
                        vS[input.index(line)].append(" ")
                        space_count = 0
                if line[i] == "[":
                    vS[input.index(line)].append(line[i+1])
                    space_count = 0

for row in vS:
    for i in range(len(row)):
        cS[i].insert(0,row[i])

for stack in cS:
    for crate in stack:
        while stack[len(stack)-1] == " ":
            stack.remove(" ")

cS2 = deepcopy(cS)
moves2 = deepcopy(moves)

for do in moves:
    for i in range(int(do[0])):
        if cS[int(do[1])-1]:
            cS[int(do[2])-1].insert(len(cS[int(do[2])-1]),cS[int(do[1])-1].pop(len(cS[int(do[1])-1])-1))

ans = ""
for stack in cS:
    if stack:
        ans = ans + stack[len(stack)-1]

print(f"p1a: {ans}")



# PART TWO
for do in moves2:
    point = len(cS2[int(do[2])-1])
    for i in range(int(do[0])):
        if cS2[int(do[1])-1]:
            cS2[int(do[2])-1].insert(point,cS2[int(do[1])-1].pop(len(cS2[int(do[1])-1])-1))

ans2 = ""
for stack in cS2:
    if stack:
        ans2 = ans2 + stack[len(stack)-1]

print(f"p2a: {ans2}")