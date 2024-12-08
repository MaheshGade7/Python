# Python program to demonstrate stack implementation using a list

# Function to push an element onto the stack
def push(stack, item):
    stack.append(item)  # Push item onto the stack
    print(f"Pushed {item} to the stack.")

# Function to pop an element from the stack
def pop(stack):
    if len(stack) == 0:
        print("Stack Underflow! No elements to pop.")
    else:
        popped_item = stack.pop()  # Remove the last item from the stack
        print(f"Popped {popped_item} from the stack.")

# Function to peek at the top element of the stack
def peek(stack):
    if len(stack) == 0:
        print("The stack is empty.")
    else:
        print(f"Top element is: {stack[-1]}")

# Function to check if the stack is empty
def is_empty(stack):
    if len(stack) == 0:
        print("The stack is empty.")
    else:
        print("The stack is not empty.")

# Main program to demonstrate the stack operations
def main():
    # Initialize an empty list to act as the stack
    stack = []
    
    while True:
        # Display the menu
        print("\nStack Operations Menu:")
        print("1. Push an element")
        print("2. Pop an element")
        print("3. Peek at the top element")
        print("4. Check if the stack is empty")
        print("5. Exit")
        
        # Get user input
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            # Push an element onto the stack
            item = input("Enter the element to push: ")
            push(stack, item)
        elif choice == '2':
            # Pop an element from the stack
            pop(stack)
        elif choice == '3':
            # Peek at the top element
            peek(stack)
        elif choice == '4':
            # Check if the stack is empty
            is_empty(stack)
        elif choice == '5':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Call the main function
if __name__ == "__main__":
    main()
