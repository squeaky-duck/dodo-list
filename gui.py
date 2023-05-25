import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("Black")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo", size=32)

add_button = sg.Button("Add", key='Add')

list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(32, 8))

edit_button = sg.Button("Edit", key='Edit')

complete_button = sg.Button("Complete", key='Complete')

exit_button = sg.Button("Exit", key='Exit')

window = sg.Window('DoDo List',
                   layout=[[clock], [label], [input_box, add_button, complete_button],
                           [list_box, edit_button],
                           [exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"]
            if new_todo.strip() == "":
                sg.popup("Please enter a todo first.", font=("Helvetica", 16))
            else:
                new_todo += "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 16))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 16))

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()

