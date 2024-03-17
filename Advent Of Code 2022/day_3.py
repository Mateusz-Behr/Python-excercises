from string import ascii_letters

with open("day_3", "r") as file:
    bags = [i for i in file.read().split("\n")]

    total = 0
    for bag in bags:
        half = len(bag)//2

        left = set(bag[:half])
        right = set(bag[half:])

        print(bag, left, right)

        for priority, char in enumerate(ascii_letters):
            if char in left and char in right:
                total += priority + 1

    print(f"First answer is: {total}")

with open("day_3", "r") as file2:
    rucksacks = "".join(file2.readlines()).split("\n")
    print(rucksacks)
    rucksacks_by_3 = [rucksacks[n:n+3] for n in range(0, len(rucksacks), 3)]
    print(rucksacks_by_3)

    total_2 = 0
    for group in rucksacks_by_3:
        first = set(group[0])
        second = set(group[1])
        third = set(group[2])

        for priority, char in enumerate(ascii_letters):
            if char in first and char in second and char in third:
                total_2 += priority + 1

    print(f"Second answer: {total_2}")



