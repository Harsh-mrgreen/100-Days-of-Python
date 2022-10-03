print('welcome to tip calculater')
total_bill = int(input('What was the total Bill ?'))
tip = int(input('what percentage tip would you like to give? 10, 12 or 15'))
people= int(input('how many peopleto split the bill ?'))

total_tip = round(((total_bill * tip) / 100) /people , 2)
print(total_tip)
final_amount = "{:.2f}".format(total_tip)