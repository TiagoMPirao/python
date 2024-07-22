import sys

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Game Choice.")
print("Your mission is to find the treasure.") 



def get_path():
    while True:
        path = input("Choose a path to follow? (Left or Right) ").strip().lower()
        if path in ("left", "right"):
            return path
        else:
            print("Invalid path. Please provide a correct path. (Left or Right)")

def get_choice(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("swim", "wait"):
            return choice
        else:
            print("Invalid input. Please provide Swim or Wait")

def get_door(prompt):
    while True:
        door = input(prompt).strip().lower()
        if door in ("red", "blue", "yellow"):
            return door
        else:
            print("Invalid input. Please provide Red or Blue or Yellow")

path = get_path()

if path == "right":
    print("You fall into a hole. Game Over!!")
    sys.exit()

choice = get_choice("You are at a lake! Now choose if you want to swim to the other side, or wait for a boat (Swim or Wait): ")

if choice == "swim":
    print("Eaten by a crocodile. Game Over!!")
    sys.exit()

door = get_door("You pass the lake! Nice! Now choose a door (Red, Yellow, Blue): ")

if door == "blue":
    print("Eaten by beasts. Game Over!!")
    sys.exit()
elif door == "red":
    print("Burned by fire. Game Over!!")
    sys.exit()
else:
    print(f"You chose the {path.capitalize()} path. Then you chose to {choice.capitalize()}, and then you decided to go through the {door.capitalize()} door. Congrats!! You Won!!")
    sys.exit()