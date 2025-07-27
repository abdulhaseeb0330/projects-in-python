
"""
Snake-Water-Gun Game:
1  Snake
-1  Water
0  Gun
"""


computer = 1

dictionary = {
    "snake": 1,
    "water": -1,
    "gun": 0
}

middle = input("Enter your choice (snake, water, gun): ").strip().lower()

if middle not in dictionary:
    print("Invalid input! Please enter snake, water, or gun.")
else:
    user = dictionary[middle]

    if user == computer:
        print("Draw!")
    elif (computer == -1 and user == 1) or (computer == 1 and user == 0) or (computer == 0 and user == -1):
        print("You win!")
    else:
        print("You lose!")

    print(f"Computer chose: {middle}")