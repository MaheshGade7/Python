class Node:
    """Class representing a node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueUsingLinkedList:
    """Class representing a queue implemented using a linked list."""
    def __init__(self):
        self.front = None  # Pointer to the front of the queue
        self.rear = None   # Pointer to the rear of the queue

    def enqueue(self, data):
        """Insert an element at the end of the queue."""
        new_node = Node(data)
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node
            print(f"Enqueued {data} into the queue.")
        else:
            self.rear.next = new_node  # Link the new node at the end
            self.rear = new_node       # Update the rear pointer
            print(f"Enqueued {data} into the queue.")

    def dequeue(self):
        """Remove an element from the front of the queue."""
        if self.front is None:  # If the queue is empty
            print("Queue is empty. Cannot dequeue.")
            return

        removed_data = self.front.data  # Data to be removed
        self.front = self.front.next    # Update the front pointer

        if self.front is None:  # If the queue becomes empty
            self.rear = None

        print(f"Dequeued {removed_data} from the queue.")

    def display(self):
        """Display all elements in the queue."""
        if self.front is None:  # If the queue is empty
            print("Queue is empty.")
            return

        print("Queue elements:")
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    """Menu-driven program to manage queue operations."""
    queue = QueueUsingLinkedList()

    while True:
        print("\nQueue Operations Using Linked List:")
        print("1. Enqueue (Insert)")
        print("2. Dequeue (Delete)")
        print("3. Display Queue")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            data = int(input("Enter the value to enqueue: "))
            queue.enqueue(data)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.display()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
