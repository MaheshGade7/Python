class Node:
    """Class representing a node in the binary search tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class representing a binary search tree."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the binary search tree."""
        if self.root is None:
            self.root = Node(key)
            print(f"Inserted {key} as the root node.")
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, current, key):
        """Helper method to insert a key recursively."""
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
                print(f"Inserted {key} to the left of {current.key}.")
            else:
                self._insert_recursively(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
                print(f"Inserted {key} to the right of {current.key}.")
            else:
                self._insert_recursively(current.right, key)

    def preorder(self, node):
        """Preorder traversal: Root -> Left -> Right."""
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        """Inorder traversal: Left -> Root -> Right."""
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        """Postorder traversal: Left -> Right -> Root."""
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

    def display_traversals(self):
        """Display all traversals."""
        print("\nPreorder Traversal:")
        self.preorder(self.root)
        print("\nInorder Traversal:")
        self.inorder(self.root)
        print("\nPostorder Traversal:")
        self.postorder(self.root)
        print()


def main():
    """Menu-driven program to interact with the BST."""
    bst = BinarySearchTree()

    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Preorder Traversal")
        print("3. Inorder Traversal")
        print("4. Postorder Traversal")
        print("5. Display All Traversals")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            key = int(input("Enter the value to insert: "))
            bst.insert(key)
        elif choice == '2':
            print("Preorder Traversal:")
            bst.preorder(bst.root)
            print()
        elif choice == '3':
            print("Inorder Traversal:")
            bst.inorder(bst.root)
            print()
        elif choice == '4':
            print("Postorder Traversal:")
            bst.postorder(bst.root)
            print()
        elif choice == '5':
            bst.display_traversals()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
