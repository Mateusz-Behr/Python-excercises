with open("day_7") as file:
    commands = [command.strip() for command in file.readlines()]

path = "/home"
dirs = {"/home":0}

# Process every command

for command in commands:

    # Commands that start with $
    if command[0] == "$":

        # Do nothing when listing directories or files
        if command[2:4] == "ls":
            pass
        # Manage changing paths
        elif command[2:4] == "cd":

             # Go back to rout
            if command[5:6] =="/":
                path = "/home"

            # Go back in the path
            elif command[5:7] == "..":
                path = path[:path.rfind("/")]

            #Change path
            else:
                dir_name = command[5:]          # Getting the name of new directory
                path = path + "/" + dir_name    # Adding to the path
                dirs.update({path:0})

    # Do nothing when listing directories available
    elif command[0:3] == "dir":
        pass

    # Get the file size and change directories in which it was found
    else:
        size = int(command[:command.find(" ")]) # Get the size of the file

        dir = path
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]

# PONIŻEJ WYPISUJE MI WSZYSTKIE SCIEŻKI \/
for dir in dirs:
    print(dir, dirs[dir])

total = 0

# Space required - space unused (total space - space used) <<minus
limit = 30000000 - (70000000 - dirs["/home"])
valid_dirs = []

for dir in dirs:

    # === PART 1 ===
    if dirs[dir] <= 100000:
        total += dirs[dir]

    # === PART 2 ===
    if limit <= dirs[dir]:
        valid_dirs.append(dirs[dir])

    smallest = min(valid_dirs)

print(f"Answer to part 1: {total}")
print(f"Answer to part 2: {smallest}")

