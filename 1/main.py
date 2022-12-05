def eat_top_elf(list):
    elf = max(nested_list, key=nested_list.get)
    print("The elf with the most calories left is...")
    print(elf)

    cals = nested_list[elf]
    print("This elf is carrying")
    print(cals)

    del nested_list[elf]
    return cals


input = open('input.txt', 'r')

nested_list = {}
elf_num = 1
for i in (row.split() for row in input):

    if not i:
        elf_num += 1
        continue

    if elf_num not in nested_list:
        nested_list[elf_num] = 0

    nested_list[elf_num] = nested_list[elf_num] + int(i[0])

top_3 = 0
top_3 += eat_top_elf(nested_list)
top_3 += eat_top_elf(nested_list)
top_3 += eat_top_elf(nested_list)

print("The top 3 elves are carrying...")
print(top_3)
