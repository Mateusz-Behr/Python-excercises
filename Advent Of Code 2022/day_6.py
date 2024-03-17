with open("day_6", "r") as file:
    code = [i for i in file.read()]

    for n in range(0, len(code) - 4):
        if len(code[n:n+4]) == len(set(code[n:n+4])):
            print(f"First answer is: {n+4}")
            break

# ===PART 2=== #
    for n in range(0, len(code) - 14):
        if len(code[n:n+14]) == len(set(code[n:n+14])):
            print(f"Second answer is: {n+14}")
            break
