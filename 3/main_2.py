def find_item(group):
    for x in group[0]:
        for y in group[1]:
            if x == y:
                for z in group[2]:
                    if x == z:
                        return x


def get_priority(item):
    addition = 0
    if item.isupper():
        addition += 26
        item = item.lower()

    addition += ord(item)-96
    return addition


def calculate_group(group):
    print(group)
    item = find_item(group)

    print(item)
    return get_priority(item)


input = open('input.txt', 'r')

priority = 0
group = []
for i in (row.split() for row in input):
    if len(group) <= 2:
        group.append(i[0])
        continue

    priority += calculate_group(group)
    group = [i[0]]

priority += calculate_group(group)

print("Total priority")
print(priority)
