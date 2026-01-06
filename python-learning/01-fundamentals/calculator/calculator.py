def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def power(a, b):
    """Raise a to the power of b."""
    return a ** b


def modulo(a, b):
    """Get remainder of a divided by b."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a % b


def floor_divide(a, b):
    """Floor division of a by b."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a // b


def display_menu():
    """Display calculator operations."""
    print("\n=== SIMPLE CALCULATOR ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulo (%)")
    print("7. Floor Division (//)")
    print("8. View History")
    print("9. Clear History")
    print("10. Recall Memory")
    print("11. Clear Memory")
    print("12. Exit")


def get_numbers():
    """Get two numbers from user with error handling."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def display_history(history):
    """Display all previous calculations."""
    if not history:
        print("\nNo calculations yet!")
        return
    
    print("\n=== CALCULATION HISTORY ===")
    for i, calc in enumerate(history, start=1):
        print(f"{i}. {calc}")
    print("=" * 30)


def save_to_history(history, num1, operator, num2, result):
    """Save a calculation to history."""
    calculation = f"{num1} {operator} {num2} = {result}"
    history.append(calculation)


def get_numbers(memory=None):
    """Get two numbers from user with error handling. Can use memory value."""
    while True:
        try:
            # First number
            num1_input = input("Enter first number (or 'M' for memory): ").strip()
            if num1_input.upper() == 'M':
                if memory is None:
                    print("Memory is empty! Please enter a number.")
                    continue
                num1 = memory
                print(f"Using memory value: {memory}")
            else:
                num1 = float(num1_input)
            
            # Second number
            num2_input = input("Enter second number (or 'M' for memory): ").strip()
            if num2_input.upper() == 'M':
                if memory is None:
                    print("Memory is empty! Please enter a number.")
                    continue
                num2 = memory
                print(f"Using memory value: {memory}")
            else:
                num2 = float(num2_input)
            
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def store_memory(value):
    """Store a value in memory."""
    print(f"Value {value} stored in memory!")
    return value


def recall_memory(memory):
    """Recall the value from memory."""
    if memory is None:
        print("Memory is empty!")
        return None
    print(f"Memory recall: {memory}")
    return memory


def clear_memory():
    """Clear memory."""
    print("Memory cleared!")
    return None



def main():
    """Main function to run the calculator."""
    print("Welcome to Simple Calculator!")
    
    # Create empty list to store calculation history
    history = []
    # Memory to store one value
    memory = None
    
    while True:
        # Show memory status in prompt
        memory_status = f" [Memory: {memory}]" if memory is not None else ""
        print(f"\n{memory_status}")
        
        display_menu()
        choice = input("\nEnter your choice (1-12): ")
        
        if choice == "12":
            print("Thank you for using Calculator. Goodbye!")
            break
        
        if choice == "8":
            display_history(history)
            continue
        
        if choice == "9":
            history.clear()
            print("History cleared!")
            continue
        
        if choice == "10":
            recall_memory(memory)
            continue
        
        if choice == "11":
            memory = clear_memory()
            continue
        
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            num1, num2 = get_numbers(memory)
            
            if choice == "1":
                result = add(num1, num2)
                operator = "+"
                print(f"\n{num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                operator = "-"
                print(f"\n{num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                operator = "×"
                print(f"\n{num1} × {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                operator = "÷"
                print(f"\n{num1} ÷ {num2} = {result}")
            elif choice == "5":
                result = power(num1, num2)
                operator = "^"
                print(f"\n{num1} ^ {num2} = {result}")
            elif choice == "6":
                result = modulo(num1, num2)
                operator = "%"
                print(f"\n{num1} % {num2} = {result}")
            elif choice == "7":
                result = floor_divide(num1, num2)
                operator = "//"
                print(f"\n{num1} // {num2} = {result}")
            
            # Save to history and memory (skip if there was an error)
            if not isinstance(result, str):
                save_to_history(history, num1, operator, num2, result)
                memory = store_memory(result)
        else:
            print("Invalid choice. Please enter 1-12.")


if __name__ == "__main__":
    main()




