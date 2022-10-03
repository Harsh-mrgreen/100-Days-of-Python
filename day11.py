import os
import random
def guessing_game(): 
  print("Welcome to the number guessing game")
  print("I am thinking a number between 1 and 100")
  ran_num = random.choice(range(1,101))
  level = input("please choose the level of difficulty: easy or hard").lower()
  if level == 'easy':
    number_of_attempts = 10
  elif level == 'hard':
    number_of_attempts = 5
  else:
    print('check your input')
    return ''
  for i in range(number_of_attempts):
      
    guess = int(input("please guess a number between 1 and 100 : "))
    
    if guess == ran_num:
      print("You have guessed the right number")
      print(guess)
      break
    else:
      if guess > ran_num:
        print('Too high, guess again')
      else:
        print('Too low, guess again')
      number_of_attempts -= 1
      print(f"Number of attempts remaining : {number_of_attempts}")

  if number_of_attempts == 0:
      print('You fail')
  

while input("Do you want to play the guessing game? y or n ").lower() == 'y':
  os.system('cls||clear')
  guessing_game()
