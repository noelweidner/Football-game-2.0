# Tony Romo's 2 Minute Drill Version 2.0 by Noel W. & Topher P.

import random

print("Welcome to Tony Romo's Two Minute Drill")
print("Your team is losing and you are on the 20 yard line.")
print("2 minutes are left on the clock to go 80 yards, score, and win the game.")
print("")

yard_line = 20
down = 1
yards_to_go = 10
game_over = False

# Super Bowl 50 Sample Data
pass_play_yards_gained = []
pass_play_yards_gained.append(18)
pass_play_yards_gained.append(6)
pass_play_yards_gained.append(0)
pass_play_yards_gained.append(22)
pass_play_yards_gained.append(0)
pass_play_yards_gained.append(1)
pass_play_yards_gained.append(0)
pass_play_yards_gained.append(7)
pass_play_yards_gained.append(7)
pass_play_yards_gained.append(0)

run_play_yards_gained = []
run_play_yards_gained.append(8)
run_play_yards_gained.append(12)
run_play_yards_gained.append(12)
run_play_yards_gained.append(-3)
run_play_yards_gained.append(2)
run_play_yards_gained.append(2)
run_play_yards_gained.append(0)
run_play_yards_gained.append(15)
run_play_yards_gained.append(2)
run_play_yards_gained.append(-8)

while game_over == False:
    if yard_line <21:
        play_selected = input("Type 1 to run or press 2 to make a pass play!")
    else:
        play_selected = input("Go again! You can still win this!!!")
    play_selected = int(play_selected)

    if play_selected == 1:
        random_number = random.randint(0, 9)
        yards_gained = run_play_yards_gained[random_number]
    else:
        random_number = random.randint(0, 9)
        yards_gained = pass_play_yards_gained[random_number]


    # Noel, you need to wrap 'yards_gained =' in an if-statement
    # Pseudo-code: if play_selected equals 1, generate a random number
    # between something and something else.
    # if play_selected equals 2, generate a different random number
    yards_to_go = yards_to_go - yards_gained
    yard_line = yard_line + yards_gained
    if yards_to_go < 0:
        down = 1
        yards_to_go = 10
        print("You gain " + str(yards_gained) + " yards.")
        print("First down!")
    else:
        down = down + 1
        print("You gain " + str(yards_gained) + " yards.")

    if yard_line >= 100:
        print("Touchdown! You Win")
        game_over = True
    elif yard_line < 100 and down > 4:
        print("Turnover on downs. You lose :(")
        game_over = True
