def perform_string_operations():
    """Perform string operations using predefined functions."""
    try:
        user_string = input("Enter a string: ")
        print("String operations:")
        print(f"Length of the string: {len(user_string)}")               # Calculate length
        print(f"String in uppercase: {user_string.upper()}")           # Convert to uppercase
        print(f"String in lowercase: {user_string.lower()}")           # Convert to lowercase
        print(f"String with first character capitalized: {user_string.capitalize()}")  # Capitalize
        print(f"String reversed: {user_string[::-1]}")                 # Reverse the string
        print(f"String with whitespace removed: {user_string.strip()}") # Remove leading/trailing spaces
        print(f"String split into words: {user_string.split()}")        # Split into words
        print(f"Does the string contain only digits? {user_string.isdigit()}")  # Check if numeric
        print(f"Does the string contain only alphabets? {user_string.isalpha()}")  # Check if alphabetic
        print(f"Replacing spaces with underscores: {user_string.replace(' ', '_')}") # Replace spaces
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    perform_string_operations()