class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Class to represent a singly linked list."""
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node at the end of the linked list."""
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            print(f"Inserted {data} as the first element.")
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node
            print(f"Inserted {data} at the end of the list.")

    def delete_node(self, key):
        """Delete a node by its value."""
        if self.head is None:  # If the list is empty
            print("List is empty. Cannot delete.")
            return

        # If the head node needs to be deleted
        if self.head.data == key:
            self.head = self.head.next
            print(f"Deleted node with value {key}.")
            return

        # Traverse the list to find the node to delete
        current = self.head
        while current.next and current.next.data != key:
            current = current.next

        if current.next is None:  # Key not found
            print(f"Node with value {key} not found.")
        else:
            current.next = current.next.next
            print(f"Deleted node with value {key}.")

    def search(self, key):
        """Search for a node by its value."""
        current = self.head
        position = 0
        while current:
            if current.data == key:
                print(f"Node with value {key} found at position {position}.")
                return
            current = current.next
            position += 1
        print(f"Node with value {key} not found in the list.")

    def print_list(self):
        """Print all elements of the singly linked list."""
        if self.head is None:
            print("The list is empty.")
            return

        print("Singly Linked List elements:")
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    """Menu-driven program to manage singly linked list operations."""
    sll = SinglyLinkedList()

    while True:
        print("\nSingly Linked List Operations:")
        print("1. Insert at end")
        print("2. Delete node by value")
        print("3. Search for a node")
        print("4. Print list")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            data = int(input("Enter the value to insert: "))
            sll.insert_at_end(data)
        elif choice == '2':
            key = int(input("Enter the value to delete: "))
            sll.delete_node(key)
        elif choice == '3':
            key = int(input("Enter the value to search for: "))
            sll.search(key)
        elif choice == '4':
            sll.print_list()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
