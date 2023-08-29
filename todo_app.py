def read_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    return tasks

def write_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

def main():
    tasks = read_tasks()
    
    while True:
        print("To-Do List App\n")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.strip()}")
        
        action = input("\nWhat would you like to do? (add/delete/quit): ").lower()
        
        if action == "add":
            new_task = input("Enter a new task: ")
            tasks.append(new_task + "\n")
            write_tasks(tasks)
        elif action == "delete":
            task_idx = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_idx < len(tasks):
                del tasks[task_idx]
                write_tasks(tasks)
            else:
                print("Invalid task number.")
        elif action == "quit":
            break
        else:
            print("Invalid action. Please choose add, delete, or quit.")

if __name__ == "__main__":
    main()
