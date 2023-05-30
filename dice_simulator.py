import random

def roll_dice():
    result = random.randint(1,6)
    print(result)

def main():
    print("welome to dice simmlator...")
    
    while True:
        roll_back = input("Enter Q to Exit else press Enter .")

        if roll_back.lower() == 'q' :
            break

        roll_dice()
    print("Thank You For Playing!")

main()


 