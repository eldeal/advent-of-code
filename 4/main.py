def contained_pairs(a, b):
    if (int(a[0]) <= int(b[0])) and (int(a[1]) >= int(b[1])):
        print("a contains b")
        return 1

    if (int(b[0]) <= int(a[0])) and (int(b[1]) >= int(a[1])):
        print("b contains a")
        return 1

    print("not contained")
    return 0


def overlapped_pairs(a, b):
    if int(a[0]) > int(b[1]):
        print("a exceeds b")
        return 0

    if (int(a[1]) >= int(b[0])):
        print("a overlaps b")
        return 1

    print("not overlapping")
    return 0


input = open('input.txt', 'r')

contained = 0
for i in (row.split(",") for row in input):
    a = i[0].split("-")
    b = i[1].strip().split("-")
    print(a)
    print(b)

    # contained += contained_pairs(a,b)
    contained += overlapped_pairs(a, b)


print("Total contained elves")
print(contained)
