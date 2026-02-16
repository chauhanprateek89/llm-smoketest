
import json

def load_todo():
    try:
        with open('./todo.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_todo(todos):
    with open('./todo.json', 'w') as file:
        json.dump(todos, file, indent=4)

def add_task(task):
    todos = load_todo()
    if task in todos:
        print("Task already exists.")
    else:
        todos.append(task)
        save_todo(todos)
        print("Task added successfully.")

def list_tasks():
    todos = load_todo()
    if not todos:
        print("No tasks to display.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(todos, start=1):
            print(f"{index}. {task}")

def mark_done(task_index):
    todos = load_todo()
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(todos):
            completed_task = todos.pop(task_index - 1)
            save_todo(todos)
            print(f"Task '{completed_task}' marked as done.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        user_input = input("\nEnter 'add', 'list', or 'done' (or 'exit' to quit): ").strip().lower()
        
        if user_input == 'exit':
            break
        
        if user_input == 'add':
            task = input("Enter the task: ")
            add_task(task)
        elif user_input == 'list':
            list_tasks()
        elif user_input == 'done':
            task_index = input("Enter the task index to mark as done: ")
            mark_done(task_index)
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
