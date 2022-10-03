from prettytable import PrettyTable

# creating object from class
table = PrettyTable()

table.add_column('Pokemon name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type',['Electric', 'Water', 'Fire'])

table.align = "l"

print(table)

