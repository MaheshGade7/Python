def reverse_string_using_list(string):
    """Reverse a given string using a list."""
    # Convert the string into a list of characters
    char_list = list(string)
    # Reverse the list
    char_list.reverse()
    # Join the characters back into a string
    reversed_string = ''.join(char_list)
    return reversed_string


# Main function to test the implementation
def main():
    # Input string from the user
    original_string = input("Enter a string to reverse: ")

    # Reverse the string
    reversed_string = reverse_string_using_list(original_string)

    # Display the reversed string
    print(f"Reversed string: {reversed_string}")


# Run the main function
if __name__ == "__main__":
    main()
