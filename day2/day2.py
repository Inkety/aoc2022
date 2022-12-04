# PART ONE

input = open("input.txt","r")
testInput = open("testInput.txt", "r")
lines = input.readlines()
testLines = testInput.readlines()

# ABC XYZ -> in order of rps for opponent and I
# ROCK GAINS 1 POINT, PAPER 2, SCISSORS 3
# LOSING GAINS 0 POINTS, DRAW IS 3, WIN IS 6

def calcPoints(moves: list) -> int:
    points = 0
    result = "-1" # w d l
    if moves[0] == "A" and moves[1] == "X":
        result = "d"
    elif moves[0] == "B" and moves[1] == "Y":
        result = "d"
    elif moves[0] == "C" and moves[1] == "Z":
        result = "d"

    elif moves[0] == "A" and moves[1] == "Z":
        result = "l"
    elif moves[0] == "B" and moves[1] == "X":
        result = "l"
    elif moves[0] == "C" and moves[1] == "Y":
        result = "l"

    elif moves[0] == "A" and moves[1] == "Y":
        result = "w"
    elif moves[0] == "B" and moves[1] == "Z":
        result = "w"
    elif moves[0] == "C" and moves[1] == "X":
        result = "w"

    if result == "d":
        points += 3
    elif result == "w":
        points += 6

    if moves[1] == "X":
        points += 1
    if moves[1] == "Y":
        points += 2
    if moves[1] == "Z":
        points += 3

    return points

games = []
for line in lines:
    moves = line.split(" ")
    games.append(moves)

games2 = []
for line in testLines:
    moves2 = line.split(" ")
    games2.append(moves2)

totalPoints = 0
for game in games:
    game[1] = game[1].replace("\n", "")
    totalPoints += calcPoints(game)

print(f"p1a: {totalPoints}")

# PART TWO

def calcReqMove(input: list) -> str: # still need to use XYZ otherwise calcPoints function does not work as intended.
    move = "-1"
    if input[1] == "X": # LOSE
        if input[0] == "A":
            move = "Z"
        if input[0] == "B":
            move = "X"
        if input[0] == "C":
            move = "Y"
    elif input[1] == "Y": # DRAW
        if input[0] == "A":
            move = "X"
        if input[0] == "B":
            move = "Y"
        if input[0] == "C":
            move = "Z"
    elif input[1] == "Z": # WIN
        if input[0] == "A":
            move = "Y"
        if input[0] == "B":
            move = "Z"
        if input[0] == "C":
            move = "X"

    return move

totalPoints = 0
for game in games:
    game[1] = game[1].replace("\n", "")
    totalPoints += calcPoints([game[0],calcReqMove(game)])

print(f"p2a: {totalPoints}")
