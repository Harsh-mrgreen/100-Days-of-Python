# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas as pd
student_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# codes = {}
#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     codes[row.letter] = row.code
    #Access row.student or row.score

codes = {row.letter:row.code for (index,row) in student_data_frame.iterrows()}
# print(codes)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# result = []
# for letter in input("enter a name: ").upper():
#     result.append(codes[letter])

result = [codes[letter] for letter in input("enter a name: ").upper()]
print(result)
