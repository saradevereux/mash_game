import os


class Results:
    def __init__(self, fortune):
        print("We've gathered all the information we need....there's no turning back now. \nYour destiny is just one button push away")
        input("Press ENTER to reveal your destiny")
        os.system("clear")
        print("\nHere it is! Your actual TRUE DESTINY\n hope its everything you ever dreamed of:\n")
        print(f"You will live in a:\n {fortune['house']}\n")
        print(f"Your mode of transportation with be:\n {fortune['transportation']}\n\n")
        print(f"Your career will be:\n {fortune['career']}\n")
        print(f"Your yearly income will be:\n {fortune['salary']}\n")
        print(f"You will live in:\n {fortune['location']}\n")
        print(f"You'll marry:\n {fortune['partner']}\n")
        print(f"For a pet, you'll have a:\n {fortune['pet']}\n")
        print(f"The number of kids you'll have:\n {fortune['kids']}\n")
        print("\nDoesn't sound so hot? \nYou could always play again.")

