# Exception handling with file operations in Python
def file_handling_example():
    try:
        # Open the file in read mode
        file_name = input("Enter the file name to read: ")
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file '{file_name}' does not exist.")

    except PermissionError:
        # Handle the case where the file exists but permission is denied
        print(f"Error: You do not have permission to access '{file_name}'.")

    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")

    finally:
        # This block will always execute
        print("File operation attempt completed.")

# Write to a file example
def write_to_file():
    try:
        # Get file name and content from user
        file_name = input("Enter the file name to write to: ")
        content = input("Enter the content to write to the file: ")

        # Open the file in write mode
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Content successfully written to '{file_name}'.")

    except PermissionError:
        # Handle permission issues
        print(f"Error: You do not have permission to write to '{file_name}'.")

    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")

    finally:
        # This block will always execute
        print("Write operation attempt completed.")

# Main function to demonstrate the file operations
def main():
    print("File Handling Operations")
    print("1. Read from a file")
    print("2. Write to a file")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        file_handling_example()
    elif choice == '2':
        write_to_file()
    else:
        print("Invalid choice. Please select either 1 or 2.")

if __name__ == "__main__":
    main()
