""" Lecture code example for lists using streets """

streets = ['Cicero', 'Harlem', 'Lake Shore Drive']  # I used street names from Chicago
print(streets)                                      # Prints ['Cicero,' 'Harlem,' 'Lake Shore Drive']

print(streets[0])                                   # prints Cicero
print(streets[1])                                   # prints Harlem
print(streets[2])                                   # prints Lake Shore Drive

streets[0] = 'Pulaski'                              # Changes Cicero to Pulaski
print(streets)                                      # prints ['Pulaski,' 'Harlem,' 'Lake Shore Drive']

streets[1] = 'Michigan'                             # Changes Harlem to Michigan
streets[2] = 'Van Buren'                            # Changes Lake Shore Drive to Van Buren
print(streets)                                      # prints ['Pulaski,' 'Michigan,' 'Van Buren']
