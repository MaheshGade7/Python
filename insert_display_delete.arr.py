# Python program to insert, delete, and display elements of an array (list)

# Function to display the elements of the array
def display_array(arr):
    if len(arr) == 0:
        print("\nThe array is empty.")
    else:
        print("\nCurrent elements in the array:")
        for i in range(len(arr)):
            print(f"Index {i}: {arr[i]}")
    print()

# Function to insert an element at a specified index
def insert_element(arr):
    try:
        index = int(input("Enter index at which to insert (0 to {}): ".format(len(arr)) ))
        if index < 0 or index > len(arr):
            print("Invalid index.")
            return
        element = input("Enter element to insert: ")
        arr.insert(index, element)
        print("Element inserted successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric index values.")

# Function to delete an element from a specified index
def delete_element(arr):
    try:
        index = int(input("Enter index of the element to delete (0 to {}): ".format(len(arr) - 1)))
        if index < 0 or index >= len(arr):
            print("Invalid index.")
            return
        deleted_value = arr.pop(index)
        print(f"Deleted element: {deleted_value}")
    except ValueError:
        print("Invalid input. Please enter numeric index values.")
    except IndexError:
        print("No element at the given index to delete.")

# Main program menu
def main():
    array = []
    while True:
        print("\nArray Operations Menu:")
        print("1. Display Array")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            display_array(array)
        elif choice == '2':
            insert_element(array)
        elif choice == '3':
            delete_element(array)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

# Call main to run the menu loop
if __name__ == "__main__":
    main()
