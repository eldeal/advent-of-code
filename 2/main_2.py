moves = {"A": {0: 3, 3: 1, 6: 2}, "B": {
    0: 1, 3: 2, 6: 3}, "C": {0: 2, 3: 3, 6: 1}}
outcome = {"X": 0, "Y": 3, "Z": 6}

input = open('input.txt', 'r')

score = 0
for i in (row.split() for row in input):
    print("Current score:")
    print(score)
    print(i)
    they = moves[i[0]]
    me = outcome[i[1]]

    score += me + they[me]

print("Total score:")
print(score)
