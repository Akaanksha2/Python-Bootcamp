############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
from art import logo
from replit import clear

print(logo)
user_cards = []
computer_cards = []
import random

def game():
  user_hand = random.sample(cards, 2)
  computer_hand = random.sample(cards, 2)
  print("Your Cards: ", user_hand)
  print("Dealer's Cards: ", computer_hand)
  
  user_sum = 0
  comp_sum = 0
  ace = 11
  blackjack = 21
  new_card = 0
  should_continue = True
  game_over = False
  
  for i in user_hand:
      user_sum += i
  
  for i in computer_hand:
      comp_sum += i
  
  if user_sum == blackjack and comp_sum == blackjack:
      #print("Draw")
      game_over = True
  
  if user_sum == blackjack:
      #print("You Win")
      game_over = True
      #exit()
  
  if comp_sum == blackjack:
      #print("You Lose")
      game_over = True
      #exit()
  
  while should_continue and game_over is False:
      if user_sum > blackjack:
          if 11 in user_hand:
              user_hand.remove(11)
              user_hand.append(1)
              user_sum -= 10
              if user_sum > 21:
                  #print("You Lose")
                  game_over = True
                  #exit()
          else:
              #print("You Lose")
              game_over = True
              #exit()
  
      if user_sum < blackjack:
          #    while should_continue:
          if user_sum < blackjack:
              prompt = input("Do you want another card? Type 'Y' or 'N'?\n")
              prompt = prompt.lower()
              if prompt == 'y':
                  new_card = random.choice(cards)
                  user_hand.append(new_card)
                  print("Your Cards: ", user_hand)
                  user_sum += new_card
                  print('Your Score is: ', user_sum)
                  if user_sum > blackjack:
                      #print("You Lose")
                      should_continue = False
                      game_over = True
                      #exit()
                  if user_sum == blackjack:
                      #print("You Won")
                      should_continue = False
                      game_over = True
                      #exit()
  
              else:
                  should_continue = False
  cnew_card = 0
  
  if comp_sum > blackjack:
      if 11 in computer_hand:
          computer_hand.remove(11)
          computer_hand.append(1)
          comp_sum -= 10
          if comp_sum > 21:
              #print("You Win")
              game_over = True
              #exit()
      else:
          #print("You Win")
          game_over = True
          #exit()
  
  while comp_sum < 17:
      cnew_card = random.choice(cards)
      computer_hand.append(cnew_card)
      print("Dealers Cards: ", computer_hand)
      comp_sum += cnew_card
      print("Dealer's Score is: ", comp_sum)
      if comp_sum > blackjack:
          #print("You Win")
          game_over = True
          #exit()
  
  if user_sum > blackjack:
      print("You Lose!!!")
  elif comp_sum > blackjack and user_sum <= blackjack:
      print("You Win!!!")
  elif user_sum == comp_sum:
      print("Draw!!!")
  elif user_sum > comp_sum and user_sum <= blackjack:
      print("You Won!!!")
  elif user_sum < comp_sum and comp_sum <= blackjack:
      print("You lose!!!")
  else:
      print("Fuck off")
  
restart = 'y'
restart = restart.lower()
while restart == 'y':
  game()
  restart = input("Do you want to restart the game? Type 'Y', 'N'. \n")

#print(comp_sum)

## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
