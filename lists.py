""" topic 7 lecture code example for modifying data in lists """
from calendar import firstweekday

# list of int values
lab_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list of float values
temps = [42, 97.9, 212, 273.15, 33.9, 90.1, 3.14]
first_day_temp = temps[0]
print(f'The first temperature referenced in my list is {first_day_temp}F')
temps[3] = 100
print(temps)

# list of different things
example = [False, 4, 3.14159265359, 'Howdy']

# list of lists?
lists = [example, temps, lab_numbers, [3,2,1]]
print(lists)

