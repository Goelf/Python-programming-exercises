#The program will first randomly generate a number unknown to the user.
#The user needs to guess what that number is.
#If the user’s guess is wrong, the program should return some sort of indication as to how wrong.
#(e.g. The number is too high or too low).
#If the user guesses correctly, a positive indication should appear.
#You’ll need functions to check if the user input is an actual number,
#to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.


import random


def compare(someinput, random_number):
    while True:
        if someinput == random_number:
            print("Bingo!")
            raise SystemExit
        else:
            if someinput > random_number:
                new_guess = int(input("Please choose a smaller number!"))
                compare(new_guess, random_number)
            else:
                new_guess = int(input("Please choose a larger number!"))
                compare(new_guess, random_number)


def main():
    input_number = int(input("Guess a number?"))
    random_number = random.choice(range(100))
    compare(input_number, random_number)

main()
