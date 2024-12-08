def file_handling_demo():
    # Write with 'w' mode
    with open("example_write.txt", "w") as file:
        file.write("This is a demonstration of write mode.\n")
        file.write("This content will overwrite any previous data.\n")
    
    # Read from file with 'r' mode
    with open("example_write.txt", "r") as file:
        print("Content read using 'r' mode:")
        print(file.read())

    # Append to the file using 'a' mode
    with open("example_write.txt", "a") as file:
        file.write("Appending a new line at the end of the file.\n")

    # Read after appending using 'r' mode
    with open("example_write.txt", "r") as file:
        print("\nContent after appending:")
        print(file.read())

    # Exclusive creation with 'x' mode
    try:
        with open("exclusive_file.txt", "x") as file:
            file.write("This file is created exclusively with 'x' mode.\n")
        print("\nExclusive file created successfully.")
    except FileExistsError:
        print("\nThe file already exists.")

    # Read and write using 'r+' mode
    with open("example_write.txt", "r+") as file:
        file.seek(0, 0)  # Go to the start of the file
        file.write("Read/Write mode demonstrates overwriting initial content.\n")
    
    # Read from file after 'r+' operations
    with open("example_write.txt", "r") as file:
        print("\nContent after 'r+' read/write operation:")
        print(file.read())

    # Binary mode operations with 'b'
    with open("binary_file.bin", "wb") as file:
        file.write(b"Binary file writing operation.\n")

    with open("binary_file.bin", "rb") as file:
        print("\nReading the binary file in binary mode:")
        print(file.read())

if __name__ == "__main__":
    file_handling_demo()
