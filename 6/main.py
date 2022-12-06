input = open('input.txt', 'r').readline()

count = 0
for i in range(len(input)):
    buffer = input[i:i+14]

    if len(set(buffer)) == 14:
        print("unique set!")
        print(buffer)
        print(i+14)
        break
