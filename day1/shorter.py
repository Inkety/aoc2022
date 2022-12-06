elfs = [0]
for line in open("input.txt","r").readlines():
    if line == "\n":
        elfs = [0] + elfs + [elfs[0]]
    else:
        elfs[0] += int(line)
print(f"p1a: {elfs.pop(elfs.index(max(elfs)))} \np2a: {elfs.pop(elfs.index(max(elfs)))+elfs.pop(elfs.index(max(elfs)))+elfs.pop(elfs.index(max(elfs)))}")