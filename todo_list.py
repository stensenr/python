def display_menu():
    """Display the main menu options."""
    print("\n=== TODO LIST ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")

def main():
    """Main function to run the todo list program."""
    print("Welcome to your Todo List!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            print("View tasks - coming soon")
        elif choice == "2":
            print("Add task - coming soon")
        elif choice == "3":
            print("Mark complete - coming soon")
        elif choice == "4":
            print("Delete task - coming soon")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()