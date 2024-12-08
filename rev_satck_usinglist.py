class Stack:
    """Class representing a stack using a list."""
    def __init__(self):
        self.stack = []

    def push(self, data):
        """Push an element onto the stack."""
        self.stack.append(data)

    def pop(self):
        """Pop an element from the stack."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        """Return the top element of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Display the elements of the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):", self.stack[::-1])

    def reverse(self):
        """Reverse the stack."""
        if not self.is_empty():
            self.stack = self.stack[::-1]
            print("Stack reversed successfully.")
        else:
            print("Cannot reverse an empty stack.")


def main():
    """Menu-driven program to demonstrate stack operations."""
    stack = Stack()

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Reverse Stack")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            data = int(input("Enter the value to push onto the stack: "))
            stack.push(data)
            print(f"Pushed {data} onto the stack.")
        elif choice == '2':
            popped_value = stack.pop()
            if popped_value is not None:
                print(f"Popped {popped_value} from the stack.")
            else:
                print("Stack is empty. Nothing to pop.")
        elif choice == '3':
            top_value = stack.peek()
            if top_value is not None:
                print(f"Top element is: {top_value}")
            else:
                print("Stack is empty.")
        elif choice == '4':
            stack.display()
        elif choice == '5':
            stack.reverse()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
