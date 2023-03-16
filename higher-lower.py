from art import logo, vs
from game_data import data
import random
import os

clear = lambda: os.system("clear")
choice = True
A = random.choice(data)
score = 0

while choice:
    print(logo)
    B = random.choice(data)

    if A == B:
        B = random.choice(data)

    nameA = A['name']
    descriptionA = A['description']
    countryA = A['country']

    QA = print(f"Compare A: {nameA}, a {descriptionA}, from {countryA} ")

    print(vs)

    nameB = B['name']
    descriptionB = B['description']
    countryB = B['country']

    QB = print(f"Against B: {nameB}, a {descriptionB}, from {countryB} ")

    #against =
    followersA = A['follower_count']
    followersB = B['follower_count']

    prompt = input("Who has more followers? Type 'A' or 'B'. \n")
    prompt = prompt.lower()

    clear()

    if prompt == 'a':
        if followersA > followersB:
            print("You are right")
            score += 1
            print(f"Your Score is: {score}")
            A = B
        else:
            print("You are wrong. Play Again!!")
            choice = False

    elif prompt == 'b':
        if followersB > followersA:
            print("You are right")
            score += 1
            print(f"Your Score is: {score}")
            A = B

        else:
            print("You are wrong. Play Again!!")
            choice = False

    else:
        print("Invalid Input")
