import functions
import PySimpleGUI as sg
import time

sg.theme("LightBrown2")

clock= sg.Text('',key='clock')
label = sg.Text("Type in a todo: ")   # Create a label on the  window
input_box = sg.InputText(tooltip = "Enter todo", key='todo')
add_button = sg.Button("Add")
list_todos = sg.Listbox(values = functions.get_todos('todos.txt'), key = 'todos',
                     enable_events = True,size = [45,10])
list_completed = sg.Listbox(values = functions.get_todos('completed_todos.txt'), key = 'c_todos',
                      enable_events = True, size = [45,10])
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
completed_button = sg.Button("Completed")
left_column_content = [[list_todos],[list_completed]]
right_column_content = [[edit_button],[delete_button],[completed_button]]
left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                  layout = [[clock],[label, input_box, add_button],[left_column,right_column],
                            [exit_button]],
                  font = ('Helvetica',15))
while True:
    event, values = window.read(timeout=200)   #time run every 10 milliseconds
    window['clock'].update(value=time.strftime("%b-%d-%Y %H:%M"))
    match event:
        case 'Add':
            todos= functions.get_todos()
            new_todo=values['todo'] + '\n' #value dari key todo
            todos.append(new_todo)
            functions.write_todos('todos.txt', todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit= values['todos'][0]
                new_todo= values['todo']+'\n'
                todos= functions.get_todos('todos.txt')
                index= todos.index(todo_to_edit)
                todos[index]= new_todo
                functions.write_todos('todos.txt',todos)
                window['todos'].update(values=todos)  # window [todos] itu mengakses list box dari window karna todos itu key dari listbox
            except IndexError:
                sg.popup("Please select an item first",font=("Helvetica", 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])  #biar bikin yg diklik muncul di input text (todo)
        case 'Delete':
            todo_to_delete= values['todos'][0]
            todos= functions.get_todos('todos.txt')
            index=todos.index(todo_to_delete)
            todos.pop(index)
            functions.write_todos('todos.txt',todos)
            window['todos'].update(values=todos)
        case "Completed":
            try:
                todo_to_complete= values['todos'][0]
                todos=functions.get_todos('todos.txt')
                index=todos.index(todo_to_complete)
                completed_todos= todos.pop(index)
                functions.write_todos('todos.txt',todos)
                c_todos= functions.get_todos('completed_todos.txt')
                c_todos.append(completed_todos)
                functions.write_todos('completed_todos.txt',c_todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
                window['c_todos'].update(values=c_todos)
                sg.popup(f'{todo_to_complete} is completed!', font=("Helvetica", 20))
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
                case
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()