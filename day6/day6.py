with open("input.txt") as file:
    input = file.read()

charCache = []
markers = []
charCache2 = []
msgMarkers = []


i = 0
for char in input:
    i += 1
    charCache.append(char)
    if len(charCache) > 4:
        del charCache[0]
    
    if len(charCache) == 4 and len(charCache) == len(set(charCache)):
        markers.append(i)
    
    charCache2.append(char)
    if len(charCache2) > 14:
        del charCache2[0]
    
    if len(charCache2) == 14 and len(charCache2) == len(set(charCache2)):
        msgMarkers.append(i)

print(f"p1a: {markers[0]}")
print(f"p2a: {msgMarkers[0]}")
