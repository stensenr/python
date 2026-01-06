import json
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def display_menu():
    """Display the main menu options."""
    print("\n=== TODO LIST ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")

def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print(f"\n{Fore.YELLOW}No tasks yet! Your list is empty.{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.CYAN}{'='*20}")
    print(f"{Fore.CYAN}   YOUR TASKS")
    print(f"{Fore.CYAN}{'='*20}{Style.RESET_ALL}")
    
    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            # Completed tasks in green with strikethrough effect
            print(f"{Fore.GREEN}{index}. [✓] {task['description']}{Style.RESET_ALL}")
        else:
            # Incomplete tasks in white
            print(f"{index}. [ ] {task['description']}")



def add_task(tasks):
    """Add a new task to the list."""
    description = input(f"\n{Fore.CYAN}Enter task description: {Style.RESET_ALL}")
    
    if description.strip():
        new_task = {
            "description": description,
            "completed": False
        }
        tasks.append(new_task)
        print(f"{Fore.GREEN}✓ Task added: '{description}'{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Task description cannot be empty!{Style.RESET_ALL}")

def mark_task_complete(tasks):
    """Mark a task as completed."""
    if not tasks:
        print(f"\n{Fore.YELLOW}No tasks to mark as complete!{Style.RESET_ALL}")
        return
    
    view_tasks(tasks)
    
    try:
        task_number = int(input(f"\n{Fore.CYAN}Enter task number to mark as complete: {Style.RESET_ALL}"))
        
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"{Fore.GREEN}✓ Task {task_number} marked as complete!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid task number. Please enter 1-{len(tasks)}.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")


def delete_task(tasks):
    """Delete a task from the list."""
    if not tasks:
        print(f"\n{Fore.YELLOW}No tasks to delete!{Style.RESET_ALL}")
        return
    
    view_tasks(tasks)
    
    try:
        task_number = int(input(f"\n{Fore.CYAN}Enter task number to delete: {Style.RESET_ALL}"))
        
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"{Fore.GREEN}✓ Deleted task: '{deleted_task['description']}'{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid task number. Please enter 1-{len(tasks)}.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")

def load_tasks():
    """Load tasks from JSON file. Returns empty list if file doesn't exist."""
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            print(f"{Fore.GREEN}✓ Loaded {len(tasks)} task(s) from file.{Style.RESET_ALL}")
            return tasks
    except FileNotFoundError:
        print(f"{Fore.YELLOW}No saved tasks found. Starting fresh!{Style.RESET_ALL}")
        return []
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error reading tasks file. Starting fresh!{Style.RESET_ALL}")
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
        print(f"{Fore.GREEN}✓ Tasks saved!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error saving tasks: {e}{Style.RESET_ALL}")


def display_menu():
    """Display the main menu options."""
    print(f"\n{Fore.CYAN}{'='*20}")
    print(f"{Fore.CYAN}   TODO LIST")
    print(f"{Fore.CYAN}{'='*20}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1.{Style.RESET_ALL} View tasks")
    print(f"{Fore.YELLOW}2.{Style.RESET_ALL} Add task")
    print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Mark task as complete")
    print(f"{Fore.YELLOW}4.{Style.RESET_ALL} Delete task")
    print(f"{Fore.YELLOW}5.{Style.RESET_ALL} Exit")

def main():
    """Main function to run the todo list program."""
    print(f"{Fore.MAGENTA}{'='*40}")
    print(f"{Fore.MAGENTA}  Welcome to your Todo List!  ")
    print(f"{Fore.MAGENTA}{'='*40}{Style.RESET_ALL}")
    
    # Load existing tasks from file
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input(f"\n{Fore.CYAN}Enter your choice (1-5): {Style.RESET_ALL}")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print(f"{Fore.MAGENTA}Goodbye!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 1-5.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()