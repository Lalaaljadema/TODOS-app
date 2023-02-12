import functions
import PySimpleGUI as sg

label= sg.Text("Type in a todo: ")   # Create a label on the  window
input_box= sg.InputText(tooltip="Enter todo", key='todo')
add_button= sg.Button("Add")
list_todos= sg.Listbox(values=functions.get_todos('todos.txt'), key='todos',
                     enable_events=True,size=[45,10])
list_completed= sg.Listbox(values=functions.get_todos('completed_todos.txt'), key='c_todos',
                      enable_events=True, size=[45,10])
edit_button=sg.Button("Edit")
delete_button=sg.Button("Delete")
completed_button=sg.Button("Completed")


window= sg.Window('My To-Do App',
                  layout=[[label, input_box, add_button],[list_todos,edit_button,delete_button,completed_button],[list_completed]],
                  font=('Helvetica',15))
while True:
    event, values= window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos= functions.get_todos()
            new_todo=values['todo'] + '\n' #value dari key todo
            todos.append(new_todo)
            functions.write_todos('todos.txt', todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit= values['todos'][0]
            new_todo= values['todo']+'\n'
            todos= functions.get_todos('todos.txt')
            index= todos.index(todo_to_edit)
            todos[index]= new_todo
            functions.write_todos('todos.txt',todos)
            window['todos'].update(values=todos)  # window [todos] itu mengakses list box dari window karna todos itu key dari listbox
        case 'Delete':
            todo_to_delete= values['todos'][0]
            todos= functions.get_todos('todos.txt')
            index=todos.index(todo_to_delete)
            todos.pop(index)
            functions.write_todos('todos.txt',todos)
            window['todos'].update(values=todos)
        case "Completed":
            todo_to_complete= values['todos'][0]
            todos=functions.get_todos('todos.txt')
            index=todos.index(todo_to_complete)
            completed_todos= todos.pop(index)
            functions.write_todos('todos.txt',todos)
            c_todos= functions.get_todos('completed_todos.txt')
            c_todos.append(completed_todos)
            functions.write_todos('completed_todos.txt',c_todos)
            window['todos'].update(values=todos)
            window['c_todos'].update(values=c_todos)
        case sg.WIN_CLOSED:
            break


window.close()