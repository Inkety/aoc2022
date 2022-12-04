# PART ONE
input = open("input.txt","r")
lines = input.readlines()

elfs = []

elf = 0
for line in lines:
    if line == "\n":
        elfs.append(elf)
        elf = 0
    else:
        elf += int(line)

print(f"p1a: {elfs.pop(elfs.index(max(elfs)))}")

# PART TWO

print(f"p2a: \
{elfs.pop(elfs.index(max(elfs)))+elfs.pop(elfs.index(max(elfs)))+elfs.pop(elfs.index(max(elfs)))}")
