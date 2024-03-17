with open("day_8", "r") as file:
    trees = [i for i in file.read().split("\n")]

ROWS = len(trees)
COLUMNS = len(trees[0])

total = 0
scores = []     #track scenic scores, part 2



edges = ROWS * 2 + (COLUMNS - 2) * 2
total = edges
print(total)

# Iterate through trees not on edges
for row in range(1, ROWS-1):
    for col in range(1, COLUMNS-1):
        tree = trees[row][col]

        #Get all horizontal & vertical trees
        left = [trees[row][col-i] for i in range(1, col+1)]
        right = [trees[row][col+i] for i in range(1, COLUMNS-col)]
        up = [trees[row-i][col] for i in range(1, row+1)]
        down = [trees[row+i][col] for i in range(1, ROWS-row)]

        ### PART 1 ###
        ## Check if the tallest tree on all sides blocks our view
        # Ile drzew po prostu widać - skądkolwiek, bez szczegółów

        if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
            total += 1

    ### PART 2 ###
        score = 1
        for lst in (left, right, up, down):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    tracker += 1
                elif lst[i] >= tree:
                    tracker += 1
                    break
                else:
                    break

            score *= tracker

        scores.append(score)

print(f"Answer for part 1 is: {total}")
print(f"Answer for part 2 is: {max(scores)}")

