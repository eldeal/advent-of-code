input = open('input.txt', 'r')

priority = 0
for i in (row.split() for row in input):
    # print("Current score:")
    print(i)
    i = i[0]
    packA = i[:len(i)//2]
    packB = i[len(i)//2:]
    print(packA)
    print(packB)

    item = ""
    for x in packA:
        for y in packB:
            if x == y:
                item = x
                break

    print(item)

    if item.isupper():
        priority += 26
        item = item.lower()

    priority += ord(item)-96

print("Total priority")
print(priority)
