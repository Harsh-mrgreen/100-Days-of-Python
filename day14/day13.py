# HIGHER OR LOWER

from game_data import data
from art import * 
import random
import os

def selection():
  option_1 = random.choice(data)
  return option_1

#def compare():

def play_game():
  print(logo)
  choice1 = selection()
  
  result = True
  win_streak = 0
  while result == True:
    choice1_name = choice1['name']
    choice1_follower = choice1['follower_count']
    print(choice1_name, choice1_follower)

    print(vs)

    choice2 = selection()
    while choice2 == choice1:
      choice2 = selection()
    choice2_name = choice2['name']
    choice2_follower = choice2['follower_count']
    print(choice2_name)

    decide = input('Please put h or l for Higher or lower').lower()
    
    if decide == 'h':
      if choice1_follower < choice2_follower:
        os.system('cls||clear')
        win_streak += 1
        choice1 = choice2
        

      else:
        print('You loose')
        print(win_streak)
        result = False
    else:
      if choice1_follower > choice2_follower:
        os.system('cls||clear')
        win_streak += 1
        choice1 = choice2
        
      else:
        print('You loose')
        print(win_streak)
        result = False

play_game()


  
