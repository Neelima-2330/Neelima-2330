tasks = []

def add_tasks():
    print("Add tasks (type 'done' when finished):")
    while True:
        task = input("Enter a task-> ")
        if task.lower() == 'done':
            break
        tasks.append(task)
        print(f"Task '{task}' added. ({len(tasks)} tasks so far)")

    print(f"\n{len(tasks)} new task(s) have been added to the list.")

def list_tasks():
    if not tasks:
        print("Currently, there are no tasks")
    else:
        print("Current Tasks-> ")
        for index, task in enumerate(tasks, start=1):  
            print(f"Task #{index}. {task}")

def delete_task():
    list_tasks()
    try:
        task_to_delete = int(input("Enter the # to delete-> "))
        if 1 <= task_to_delete <= len(tasks):  
            tasks.pop(task_to_delete - 1)  
            print(f"Task #{task_to_delete} has been deleted.")
        else:
            print(f"Task #{task_to_delete} was not found. Please enter a number between 1 and {len(tasks)}.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the to-do list app!")
    choices = {
        "1": add_tasks,
        "2": delete_task,
        "3": list_tasks,
    }
    
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add new tasks")
        print("2. Delete a task")
        print("3. List the tasks")
        print("4. Quit")
        
        choice = input('Enter your choice-> ')
        
        if choice in choices:
            choices[choice]()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid. Please try again.")

if __name__ == "__main__":
    main()
