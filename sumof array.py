# Function to compute the sum of elements in an array
def find_sum(arr):
    total = 0
    for num in arr:
        total += num  # Add each element to total
    return total


# Function to display the array and its sum
def main():
    # Input size of the array from the user
    n = int(input("Enter the number of elements in the array: "))
    
    # Input array elements from the user
    arr = []
    print("Enter the elements of the array:")
    for i in range(n):
        element = int(input())
        arr.append(element)

    # Display the entered array
    print("\nArray elements:")
    print(arr)

    # Calculate the sum of elements
    result = find_sum(arr)

    # Display the sum
    print(f"\nSum of all elements in the array: {result}")


# Call the main function
if __name__ == "__main__":
    main()
