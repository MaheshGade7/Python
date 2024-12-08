def binary_search(arr, target):
    """
    Perform binary search on a sorted list (array) to find the target value.
    
    Args:
    arr (list): The sorted list to search in.
    target (int): The value to search for.

    Returns:
    int: The index of the target if found; otherwise, -1.
    """
    low, high = 0, len(arr) - 1  # Initialize search range
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index

        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid  # Target found
        elif arr[mid] < target:
            # Adjust the search range to the right half
            low = mid + 1
        else:
            # Adjust the search range to the left half
            high = mid - 1

    # Target not found
    print(f"{target} not found in the array.")
    return -1


def main():
    """Main function to test binary search."""
    # Input a sorted array
    arr = list(map(int, input("Enter a sorted list of numbers separated by spaces: ").split()))
    
    # Input the number to search
    target = int(input("Enter the number you want to search for: "))

    # Perform binary search
    index = binary_search(arr, target)
    
    if index != -1:
        print(f"Index of {target}: {index}")
    else:
        print("The number was not found in the array.")


if __name__ == "__main__":
    main()
