def tally(score, move, result):
    score += move
    score += outcome[result]
    return score


moves = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
outcome = {"lose": 0, "draw": 3, "win": 6}

input = open('input.txt', 'r')

score = 0
for i in (row.split() for row in input):
    print("Current score:")
    print(score)
    print(i)
    they = moves[i[0]]
    me = moves[i[1]]

    print(str(they) + " vs " + str(me))

    if they == me:
        score += me + outcome["draw"]
        continue

    if (me == 1 and they == 3) or (me == 2 and they == 1) or (me == 3 and they == 2):
        score += me + outcome["win"]
        continue

    score += me + outcome["lose"]

print("Total score:")
print(score)
