class File(object):
    def __init__(self, name, size, child):
        self.name = name
        self.size = size
        self.children = [child]


def add_file(c):
    if c[0] == "dir":
        stack.append(File(c[1], 0))
    else:
        stack.append(File(c[1], c[0]))


input = open('input.txt', 'r')

commands = []
for i in (row.split() for row in input):
    commands.append(i)

stack = []
for c in range(len(commands)):
    if c[0] == "$" and c[1] == "cd" and c[2] != "..":
        # moving into a directory

    if c[0] == "$" and c[1] == "cd" and c[2] == "..":
        # moving out of a directory

    if c[0] == "$" and c[1] == "ls":
        # listing files in a directory

    add_file(stack, c)
