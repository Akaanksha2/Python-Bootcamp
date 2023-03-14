############### Blackjack Project ####################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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



