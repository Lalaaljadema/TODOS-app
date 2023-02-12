from functions import get_todos, write_todos
import time

now= time.strftime("%b-%d-%Y %H:%M")
print("The time is below:")
print("it is", now)
while True:
    user_action = input("type add, show, edit, complete, reset, delete, remove, exit:")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo + '\n')

        write_todos('todos.txt', todos)
    elif user_action.startswith('show'):
        todos = get_todos()

        print("your todos:")
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f'{index+1}-{item}')

        c_todos = get_todos('completed_todos.txt')
        print('completed todos')
        for index, c_item in enumerate(c_todos):
            c_item = c_item.strip('\n')
            print(f'{index + 1}-{c_item}')
        write_todos('completed_todos.txt', c_todos)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number-1
            todos = get_todos()
            new_todo = input('Enter a new todo:') + '\n'
            todos[number] = new_todo
            write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number-1   
            todos_to_remove = todos[index].strip('\n')

            completed_item = todos.pop(index)
            write_todos('todos.txt', todos)
            message = f'{todos_to_remove.strip()} has been removed from the list'
            print(message)
            c_todos = get_todos('completed_todos.txt')
            c_todos.append(completed_item)

            write_todos('completed_todos.txt', c_todos)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith('delete'):
        user_input = input("delete todos or completed?:")
        if user_input == 'todos':
            todos = get_todos()
            todos.clear()
            write_todos('todos.txt', todos)
        elif user_input == 'completed':
            c_todos = get_todos('completed_todos.txt')
            c_todos.clear()
            write_todos('completed_todos.txt', c_todos)
        else:
            print("unknown command")
    elif user_action.startswith('reset'):
        todos = get_todos()
        todos.clear()
        write_todos('todos.txt', todos)
        c_todos = get_todos('completed_todos.txt')
        c_todos.clear()
        write_todos('todos.txt', todos)

        print("all files have been deleted")
    elif user_action.startswith('remove'):
        todos = get_todos('todos.txt')
        c_todos = get_todos('completed_todos.txt')
        user_input = input('remove todos or completed?:')
        if user_input == "todos":
            todos_len = len(todos)
            if todos_len:
                number = int(input('number of todos to be removed:'))
                remove_todos = todos.pop(number-1)
                write_todos('todos.txt', todos)
            else:
                print('todos is empty')
        elif user_input == "completed":
            completed_len = len(c_todos)
            if completed_len:
                number = int(input('number of completed to be removed:'))
                remove_completed = c_todos.pop(number-1)
                write_todos('completed_todos.txt', c_todos)
            else:
                print('completed todos is empty')

    elif user_action.startswith('exit'):
        break
    else:
        print('wrong command')
print('Bye!')
