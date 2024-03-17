import re
with open("day_4", "r") as file:

    pairs = [int(i) for i in re.split('[- ,\n]', file.read())]

    pairs_by_4 = [pairs[n:n+4] for n in range(0, len(pairs), 4)]

    counter = 0
    for group in pairs_by_4:
        if (group[0] <= group[2] and group[1] >= group[3]) or (group[2] <= group[0] and group[3] >= group[1]):
            counter += 1

    print(f"First answer is: {counter}")

    counter_2 = 0
    for group in pairs_by_4:
        if group [2] <= group[0] <= group[3] or group [2] <= group[1] <= group[3] or group [0] <= group[2] <= group[1] or group [0] <= group[3] <= group[1]:
            counter_2 += 1

    print(f"Second answer is: {counter_2}")

#2 inaczej
with open("day_4", "r") as file:
    data = [i for i in file.read().strip().split("\n")]
    # print(data)

    pairs = 0
    for entry in data:
        first, second = entry.split(",")

        first = [int(i) for i in first.split("-")]
        second = [int(i) for i in second.split("-")]

        if first[0] <= second[0] and first[1] >= second[1]:
            pairs += 1
        elif second[0] <= first[0] and second[1] >= first[1]:
            pairs += 1

    print(f"First answer with another solution: {pairs}")