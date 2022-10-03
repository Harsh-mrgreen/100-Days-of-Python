# BLACK JACK

import random
#from replit import clear
#from art import logo


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  rand_card = random.choice(cards)
  return rand_card

def calculate_score(b_cards):
      score = sum(b_cards)

      if score == 21 and len(b_cards) == 2:
        return 0

      if 11 in b_cards and score > 21:
        b_cards.remove(11)
        b_cards.append(1)
        score = sum(b_cards)
      return score



def compare(user_score, computer_score):

  if user_score == computer_score:
    return 'Its a Draw'
  elif computer_score == 0:
    return 'You loose'
  elif user_score == 0:
    return 'You win'
  elif user_score > 21:
    return 'You loose'
  elif computer_score > 21:
    return 'You win'
  else:
    if user_score > computer_score:
      return 'User wins'
    else:
      return 'You loose'



def play_game():
  print(logo)
  is_game_over = False
  user_cards = []
  computer_cards = []
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  print(f"user_cards : {user_cards}")
  print(f"computer_cards : {computer_cards[0]}")
  print('deal cards done') 
  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    if user_score == 0 or  computer_score == 0 or user_score > 21:
      is_game_over = True

  
    else:
      another_card = input('DO you want to draw another card? y or n ').lower()
      if another_card == 'y':
        user_cards.append(deal_card())
        print(f"user_cards : {user_cards}")

  
      else:
        is_game_over = True
  

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)  

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
  




