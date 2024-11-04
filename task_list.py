"""Program to add items to a list"""

todo_list = []                  # an empty list

while True:
    task = input('Enter a task, or press enter to stop: ')
    if task:                    # an emtpy string is False
        if task in todo_list:
            print('You have already added this task')
        else:
            todo_list.append(task)  # add task to end of todo_list
    else:
        break                   # loop will end if user inputs emtpy string

print('Thank you. Your tasks are: ')

for index, task in enumerate(todo_list):
    print(f'Task {index+1} is {task}')                 # prints the tasks

#number_of_tasks = len(todo_list)
print(f'You have {len(todo_list)} tasks to do today')
