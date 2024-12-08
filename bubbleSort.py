def bubble_sort(numbers):
    """
    Sorts a list of numbers in ascending order using the Bubble Sort algorithm.
    
    Args:
    numbers (list): The list of numbers to sort.

    Returns:
    None: The list is sorted in-place.
    """
    n = len(numbers)
    for i in range(n - 1):
        # Track if any swaps occur; optimization to stop early if sorted
        swapped = False
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                # Swap if the current element is greater than the next
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        
        # If no swaps occurred in this pass, the list is already sorted
        if not swapped:
            break

def main():
    """Main function to demonstrate Bubble Sort."""
    print("Bubble Sort Algorithm")
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Original List:", numbers)
    
    bubble_sort(numbers)
    print("Sorted List:", numbers)

if __name__ == "__main__":
    main()
