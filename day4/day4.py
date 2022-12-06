# PART ONE

with open("input.txt", "r") as file:
    input = file.read().split("\n")

def between(i1: int, i2: tuple) -> bool:
    if i1 >= i2[0] and i1 <= i2[1] or i1 <= i2[0] and i1 >= i2[1]:
        return True

overlaps = 0
fullContains = 0
for duo in input:
    elves = duo.split(",")
    e1 = elves[0].split("-")
    e2 = elves[1].split("-")
    e1 = [int(e1[0]), int(e1[1])]
    e2 = [int(e2[0]), int(e2[1])]
    if e1[0] >= e2[0] and e1[1] <= e2[1] or e2[0] >= e1[0] and e2[1] <= e1[1]:
        fullContains += 1

    # PART TWO

    if between(e1[0],e2) or between(e1[1],e2) or between(e2[0],e1) or between(e2[1],e1):
        overlaps += 1

print(f"p1a: {fullContains}")
print(f"p2a: {overlaps}")