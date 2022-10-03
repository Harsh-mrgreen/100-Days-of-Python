from replit import clear
from art import * 


print(logo)
print("Welcome to the secret auction program")

silent_auc = {}
def auction():

  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n"))
  silent_auc[name] = bid

  others_bid = input("Are there any other bidders? Type yes or no\n").lower()
  if others_bid == 'yes':
    clear()
    auction()
  else:
    clear()
    highest = max(list(silent_auc.values()))
    #for bid in silent_auc:
    for bids in silent_auc:
      if silent_auc[bids] == highest:
        print(bids, highest)

auction()
