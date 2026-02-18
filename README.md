# Todo List Application

This is a simple command-line application that allows you to manage your tasks efficiently. It uses a JSON file (`./todo.json`) to store the list of tasks.

## How to Use

1. **Add a Task:**
   - Open the terminal and navigate to the project directory.
   - Run the following command:
     ```bash
     python app.py add "Task Description"
     ```
   - Replace `"Task Description"` with your task's description.

2. **View Tasks:**
   - To see all tasks, run:
     ```bash
     python app.py list
     ```

3. **Mark a Task as Completed:**
   - To mark a specific task as completed, use:
     ```bash
     python app.py complete <task_id>
     ```
   - Replace `<task_id>` with the ID of the task you want to mark as completed.

4. **Remove a Task:**
   - To remove a task, run:
     ```bash
     python app.py remove <task_id>
     ```
   - Replace `<task_id>` with the ID of the task you want to remove.

## File Structure

- `app.py`: The main script that handles user input and interacts with the JSON file.
- `todo.json`: A JSON file used to store tasks. It has the following structure:
  ```json
  {
    "tasks": [
      {
        "id": 1,
        "description": "Complete project report",
        "completed": false
      },
      {
        "id": 2,
        "description": "Read a book on Python programming",
        "completed": true
      }
    ]
  }
  ```

## Contributing

Feel free to contribute by adding new features or fixing bugs. Please submit your pull requests with clear descriptions of the changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
