""" Lecture code example for lists using streets """

streets = ['Cicero', 'Harlem', 'Lake Shore Drive']  # I used street names from Chicago
print(streets)                                      # Prints ['Cicero,' 'Harlem,' 'Lake Shore Drive']
                                                    # I took the time to figure out how to comment out and hide a block of code like in the video
# #print(streets[0])                                   # prints Cicero
# #print(streets[1])                                   # prints Harlem
# #print(streets[2])                                   # prints Lake Shore Drive
#
# streets[0] = 'Pulaski'                              # Changes Cicero to Pulaski
# #print(streets)                                      # prints ['Pulaski,' 'Harlem,' 'Lake Shore Drive']
#
# streets[1] = 'Michigan'                             # Changes Harlem to Michigan
# streets[2] = 'Van Buren'                            # Changes Lake Shore Drive to Van Buren
# print(streets)                                     # prints ['Pulaski,' 'Michigan,' 'Van Buren']

for street in streets:
    print(street)

delivery_instructions = 'Please deliver to these streets:'

for street in streets:
    delivery_instructions = delivery_instructions + street + ', '

print(delivery_instructions)
