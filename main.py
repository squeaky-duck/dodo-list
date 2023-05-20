# from functions import get_todos, write_todos
import functions
while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()
    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"
        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)

        except ValueError:
            print("Your Command is not Valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            index = int(user_action[9:]) - 1
            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list.")
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Next time, enter a valid command you stupid duck!")
print("Bye")
