import functions
import PySimpleGUI as sg

label= sg.Text("Type in a todo: ")   # Create a label on the  window
input_box= sg.InputText(tooltip="Enter todo", key='todo')
add_button= sg.Button("Add")



window= sg.Window('My To-Do App',
                  layout=[[label, input_box, add_button]],
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
        case ''
        case sg.WIN_CLOSED:
            break


window.close()