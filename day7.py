#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

import random
print(stages[6])
chosen_word = random.choice(word_list)
lives = 6

word = ''

for i in range(len(chosen_word)):
  word += '_'
  
print(word + '\n')
word = list(word)

while '_' in word:

  guess = input('please guess a  letter ').lower()
  if guess in word:
    print('abe gadhe dhyaan se khel')

  if guess in chosen_word:
    print('Present')
    #word = word.replace(word[ind],guess)
    ind = []
    for i in range(len(chosen_word)):
      if chosen_word[i] == guess:
        ind.append(i)
    
    for j in ind:
      word[j] = guess

    print(word)
  
  else:
    print(f"This {guess} is not in the chosen_word")
    lives -= 1
    print(stages[lives])
    if lives == 0:
      print('You loose')
      break
  

else:
  print('You win')
  word = ''.join(word)
  print(word)

