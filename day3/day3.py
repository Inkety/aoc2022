# PART ONE

with open("input.txt", "r") as file:
    string = file.read()
    input = string.split("\n")
    input2 = input.copy()

rucksacks = []
for line in input:
    midPoint = int((len(line)/2))
    rucksacks.append([line[0:midPoint],line[midPoint:len(line)]])

global lower, upper
lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def convPoints(char: str) -> int:
    global upper, lower
    if char.isupper():
        value = upper.index(char) + 26 + 1
    else:
        value = lower.index(char) + 1
    return int(value)

# PRIORITIES FOR LOWERCASE LETTERS 1-26, UPPERCASE 27-52
totalPriority = 0
for rucksack in rucksacks:
    alreadyRan = False
    for char in rucksack[0]:
        if char in rucksack[1] and not alreadyRan:
            totalPriority += convPoints(char)
            alreadyRan = True

print(f"p1a: {totalPriority}")

# PART TWO

groups = []
while input2:
    groups.append([input2.pop(0),input2.pop(0),input2.pop(0)])

totalBadgePriority = 0
for group in groups:
    alreadyRan = False
    for char in group[0]:
        if char in group[1] and char in group[2] and not alreadyRan:
            totalBadgePriority += convPoints(char)
            alreadyRan = True

print(f"p2a: {totalBadgePriority}")
