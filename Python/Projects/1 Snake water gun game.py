import random


def GameWin(comp, you):
    # if both values are equal declare tie
    if comp == you:
        return None

    # check for all possibilities whe computer choose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    # check for all possibilities whe computer choose w
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

    # check for all possibilities whe computer choose g
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False


print("Comp Turn: Snake(s) Water(w) or Gun(g)?")

randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(s)?")

a = GameWin(comp, you)

print(f"Computer Choose {comp}")

print(f"Computer Choose {you}")

if a == None:
    print("The game is Tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
