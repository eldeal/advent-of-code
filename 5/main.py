#                     [Q]     [P] [P]
#                 [G] [V] [S] [Z] [F]
#             [W] [V] [F] [Z] [W] [Q]
#         [V] [T] [N] [J] [W] [B] [W]
#     [Z] [L] [V] [B] [C] [R] [N] [M]
# [C] [W] [R] [H] [H] [P] [T] [M] [B]
# [Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
# [B] [R] [B] [C] [D] [H] [D] [C] [N]
#  1   2   3   4   5   6   7   8   9

stacks = {1: ["B", "Q", "C"],
          2: ["R", "Q", "W", "Z"],
          3: ["B", "M", "R", "L", "V"],
          4: ["C", "Z", "H", "V", "T", "W"],
          5: ["D", "Z", "H", "B", "N", "V", "G"],
          6: ["H", "N", "P", "C", "J", "F", "V", "Q"],
          7: ["D", "G", "T", "R", "W", "Z", "S"],
          8: ["C", "G", "M", "N", "B", "W", "Z", "P"],
          9: ["N", "J", "B", "M", "W", "Q", "F", "P"]}


input = open('input.txt', 'r')

contained = 0
for i in (row.split() for row in input):
    num = i[1]
    fr = int(i[3])
    to = int(i[5])
    print(i)

    # part 1
    # for m in range(int(num)):
    #     stacks[to].append(stacks[fr].pop())

    # part 2
    shift = []
    for m in range(int(num)):
        shift.insert(0, stacks[fr].pop())

    stacks[to].extend(shift)

output = []
for i in range(1, 10):
    output.append(stacks[i].pop())


print(output)
