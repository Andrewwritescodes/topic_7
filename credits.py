""" Lecture code example """

credits_per_class = [4, 3, 3, 2]

# total = 0
#
# for credit_count in credits_per_class:
#     total = total + credit_count
#     print(f'{credit_count}, total so far {total}')

#print(total)

total_with_sum_function = sum(credits_per_class)
print(total_with_sum_function)

# if total >= 12:
#     print('You are full time')
# elif total >= 6:
#     print('You are part time')
# else:
#     print('You are less than part time')