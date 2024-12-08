def find_second_maximum(arr):
    """Function to find the second maximum number in an array."""
    if len(arr) < 2:
        return "Array must have at least two elements."

    # Initialize the maximum and second maximum
    max_num = second_max = float('-inf')

    for num in arr:
        if num > max_num:
            second_max = max_num  # Update second maximum
            max_num = num         # Update maximum
        elif num > second_max and num != max_num:
            second_max = num       # Update second maximum if it’s less than max

    if second_max == float('-inf'):
        return "No second maximum (all elements may be the same)."

    return second_max


# Main function to test the implementation
def main():
    # Input array from the user
    n = int(input("Enter the number of elements in the array: "))
    arr = []
    print("Enter the elements of the array:")
    for _ in range(n):
        arr.append(int(input()))

    # Display the entered array
    print("\nArray:", arr)

    # Find the second maximum
    result = find_second_maximum(arr)

    # Display the result
    print(f"Second maximum number in the array: {result}")


# Run the main function
if __name__ == "__main__":
    main()
