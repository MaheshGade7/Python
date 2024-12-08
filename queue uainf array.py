class Queue:
    """Class to implement a queue using an array (list in Python)."""
    def __init__(self, capacity):
        self.queue = [None] * capacity  # Initialize the queue with a fixed size
        self.front = -1  # Points to the front of the queue
        self.rear = -1   # Points to the rear of the queue
        self.capacity = capacity  # Maximum size of the queue

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front == -1

    def is_full(self):
        """Check if the queue is full."""
        return self.rear == self.capacity - 1

    def enqueue(self, data):
        """Insert an element into the queue."""
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return

        if self.front == -1:  # First element being inserted
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = data
        print(f"Enqueued {data} into the queue.")

    def dequeue(self):
        """Remove an element from the front of the queue."""
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None

        removed_data = self.queue[self.front]
        self.queue[self.front] = None  # Clear the slot

        if self.front == self.rear:  # Queue becomes empty after this operation
            self.front = self.rear = -1
        else:
            self.front += 1

        print(f"Dequeued {removed_data} from the queue.")
        return removed_data

    def display(self):
        """Display the elements in the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


def main():
    """Menu-driven program to demonstrate queue operations."""
    capacity = int(input("Enter the capacity of the queue: "))
    queue = Queue(capacity)

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue (Insert)")
        print("2. Dequeue (Remove)")
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
