import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elaenor", "Freddie"]
# new_names = [name.upper() for name in names if (len(name) > 5)]
# print(new_names)
marks = {name:random.randint(1,100) for name in names}

passed_students  = {student:score for (student, score) in marks.items() if score  > 60}
print(passed_students)
