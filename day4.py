import random

choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
random_choice = random.randint(0,2)

if random_choice == choice:
  print('do it again')

elif choice == 0:
  if random_choice == 1:
    print('You win')
  else:
    print('You loose')
  
elif choice == 1:
  if random_choice == 0:
    print('You win')
  else:
    print('You loose')
else:
  if random_choice == 0:
    print('You Loose')
  else:
    print('You win')

print(f"choice : {choice}\n random_choice: {random_choice}\n")
