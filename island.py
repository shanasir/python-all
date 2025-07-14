print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("welcome to the tresure island .")
print("your mission is to find the tresure.")
choice1 = input('you are at crossroad where do yo want to go? type left or right.\n').lower()

if choice1 == "left":
    choice2 = input(
        'you come to a lake.there is an isalnd in the middle of the lake.type "wait" to wait for a boat.type "swim"to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input(
            "you arrive at the isalnd unharmed . to continue (or) win,you need to guess a right door... so there are 3 doors infront you choose correct one to pass (or) win the game ...so the doors are .One red ,One blue and yellow\n").lower()
        if choice3 == "red":
            print("you are dead")
        elif choice3 == "yellow":
            print("you won the game ! congraluations")
        elif choice3 == "blue":
            print("you are dead")
        else:
            print("invalid choice")
    else:
        print("you are dead")
else:
    print("you are dead")



