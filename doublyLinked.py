class Node:
    """Class to represent a node in the doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Class to represent a doubly linked list."""
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            print(f"Inserted {data} as the first element.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        print(f"Inserted {data} at the end of the list.")

    def delete_node(self, key):
        """Delete a node by its value."""
        if not self.head:  # If the list is empty
            print("List is empty. Cannot delete.")
            return
        current = self.head
        while current:
            if current.data == key:
                if current.prev:  # If it's not the head node
                    current.prev.next = current.next
                if current.next:  # If it's not the tail node
                    current.next.prev = current.prev
                if current == self.head:  # If it's the head node
                    self.head = current.next
                print(f"Deleted node with value {key}.")
                return
            current = current.next
        print(f"Node with value {key} not found.")

    def search(self, key):
        """Search for a node by its value."""
        current = self.head
        index = 0
        while current:
            if current.data == key:
                print(f"Node with value {key} found at position {index}.")
                return
            current = current.next
            index += 1
        print(f"Node with value {key} not found in the list.")

    def print_list(self):
        """Print the elements of the doubly linked list."""
        if not self.head:  # If the list is empty
            print("The list is empty.")
            return
        print("Doubly Linked List elements:")
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


def main():
    """Menu-driven program to manage doubly linked list."""
    dll = DoublyLinkedList()

    while True:
        print("\nDoubly Linked List Operations:")
        print("1. Insert at end")
        print("2. Delete node by value")
        print("3. Search for a node")
        print("4. Print list")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            data = int(input("Enter the value to insert: "))
            dll.insert_at_end(data)
        elif choice == '2':
            key = int(input("Enter the value to delete: "))
            dll.delete_node(key)
        elif choice == '3':
            key = int(input("Enter the value to search for: "))
            dll.search(key)
        elif choice == '4':
            dll.print_list()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
