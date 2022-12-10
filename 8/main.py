def check_height(tree, biggest):
    if tree["height"] > biggest["height"]:
        if tree["visible"] == False:
            tree["visible"] = True
        biggest = tree
    return biggest, tree

def output(rows):
    count = 0
    for row in rows:
        p = []
        for tree in row:
            if tree["visible"] == True:
                count += 1
                p.append(tree["height"])
            else:
                p.append("-")
        print(p)
    print("Counted in rows and columns")
    print(count)

base_tree = {"height":-1}
input = open('input.txt', 'r')

rows = []
for i in (row.split() for row in input):
    r = []
    for l in i[0]:
        r.append({"height": l, "visible": False})

    rows.append(r)

for row_num, row in enumerate(rows):
    # left to right
    biggest = base_tree
    for col in range(len(row)):
        biggest, rows[row_num][col] = check_height(row[col], biggest)

    # right to left
    biggest = base_tree
    for col in range(len(row)-1, -1, -1):
        print(col)
        biggest, rows[row_num][col] = check_height(row[col], biggest)

for col in range(0, len(rows[0])):
    # top to bottom
    biggest = base_tree
    for row_num in range(len(rows)):
         biggest, rows[row_num][col] = check_height(rows[row_num][col], biggest)

    # bottom to top
    biggest = base_tree
    for row_num in range(len(rows)-1, -1, -1):
        biggest, rows[row_num][col] = check_height(rows[row_num][col], biggest)

output(rows)
