#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100.")

def game():
  
  choice = input("Choose a difficulty. Type 'Easy' or 'Hard': \n")
  
  choice = choice.lower()
  
  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
  number = random.choice(range(1, 101))
  print(number)
  
  if choice == 'easy':
      attempt = 10
  elif choice == 'hard':
      attempt = 5
    
  print(f"You have {attempt} attempts remaining to guess the number")
  for i in range(1, attempt + 1):
        guess = int(input("Make a guess: \n"))
        attempt -= 1
        if guess == number:
            print("You guessed it right")
            break
        elif guess < number:
            print("Too Low")
            print(f"You have {attempt} guesses left.")
        elif guess > number:
            print("Too High")
            print(f"You have {attempt} guesses left.")
  
start = True

while start:
  game()
  restart = input("Do you want to restart the game? Type 'y' or 'n' \n")
  if restart == 'n':
    start = False
  
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
