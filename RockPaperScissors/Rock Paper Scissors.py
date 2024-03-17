import time
import random

rock_paper_scissors = ['R', 'P', 'S']
proper_data = ['R', 'P', 'S', 'EXIT', 'ROCK', 'PAPER', 'SCISSORS']
victory = [['R', 'S'], ['P', 'R'], ['S', 'P']]
lose = [['R', 'P'], ['P', 'S'], ['S', 'R']]


print("Welcome to the Rock Paper Scissors game! Let's play to 3 points total.")
time.sleep(1)
print("You can type exit in any time to close the game.")
time.sleep(1)


player_score = 0
cpu_score = 0
result = []

while True:

    result.clear()

    player_choice = input("\tPlease, choice one: (R)ock, (P)aper, (S)cissors.\n").upper()
    player_choice_name = ('Rock' if player_choice[0] == 'R'
        else 'Scissors' if player_choice[0] == 'S'
        else 'Paper' if player_choice[0] == 'P'
        else 'X')
    cpu_choice = random.choice(rock_paper_scissors)
    cpu_choice_name = ('Rock' if cpu_choice == 'R'
        else 'Scissors' if cpu_choice == 'S'
        else 'Paper' if cpu_choice == 'P'
        else 'Z')

    result.append(player_choice[0])
    result.append(cpu_choice)

    if player_choice == cpu_choice:
        print(f"Player chose {player_choice_name}, Computer chose {cpu_choice_name}")
        time.sleep(1)
        print("Draw")
        time.sleep(1)
        continue
    elif result in victory:
        player_score += 1
        print(f"Player chose {player_choice_name}, Computer chose {cpu_choice_name}")
        time.sleep(1)
        print(f"Player wins"
              f"\tPlayer {player_score} : Computer {cpu_score}")
        time.sleep(1)
        if player_score == 3:
            break
        else:
            continue
    elif result in lose:
        cpu_score += 1
        print(f"Player chose {player_choice_name}, Computer chose {cpu_choice_name}")
        time.sleep(1)
        print(f"Computer wins"
              f"\tPlayer {player_score} : Computer {cpu_score}")
        time.sleep(1)
        if cpu_score == 3:
            break
        else:
            continue
    elif player_choice not in proper_data:
        print("Please type a proper data - (R)ock, (P)aper, (S)cissors or EXIT.")
        time.sleep(1)
        continue
    elif player_choice == 'EXIT':
        print('Closing the game.')
        time.sleep(1)
        exit()

if player_score == 3:
    print('-' * 30)
    print('You won, congratulations!')
    time.sleep(1)
    print("Closing the game")
    exit()
else:
    print('-' * 30)
    print('Computer won, good luck in next game!')
    time.sleep(1)
    print("Closing the game")
    exit()

