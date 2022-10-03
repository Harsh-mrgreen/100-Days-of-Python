#four keywords in catching exceptions and errors:-
#try - somthing that might cause an exception
#except - Do this if there was an exception
#else: - Do this if there were no exceptions
#finally  - Do this no matter what happens
#raise - allows us to raise our own exception

# to work with json data -
# To write -  json.dump()
# To read - json.load()
# to Update - json.update()


height = float(input("please enter your height"))
weight = int(input("Please enter your weight"))

if height > 3:
    raise ValueError("human height should not be over 3 meters.")


BMI = weight / height ** 2
print(BMI)
