# Function to convert a given matrix to its sparse matrix representation
def to_sparse_matrix(matrix):
    # Get the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Initialize list for sparse matrix with header row
    # The first row contains [total_rows, total_columns, number_of_non_zero_elements]
    sparse = []
    
    # Count the number of non-zero elements in the matrix
    non_zero_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                non_zero_count += 1

    # First row of the sparse matrix: [rows, columns, number of non-zero elements]
    sparse.append([rows, cols, non_zero_count])

    # Add each non-zero element as a triplet: [row_index, col_index, value]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse.append([i, j, matrix[i][j]])

    return sparse


# Function to display a matrix
def display_matrix(matrix):
    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)


# Function to display the sparse matrix in triplet form
def display_sparse_matrix(sparse_matrix):
    print("\nSparse Matrix Representation (triplets):")
    for row in sparse_matrix:
        print(row)


# Main program
def main():
    # Input matrix from the user
    rows = int(input("Enter number of rows in the matrix: "))
    cols = int(input("Enter number of columns in the matrix: "))

    # Create the matrix by taking user input
    matrix = []
    print("\nEnter the elements of the matrix row by row:")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Error: Incorrect number of columns. Please re-enter this row.")
            return
        matrix.append(row)

    # Display the original matrix
    display_matrix(matrix)

    # Convert the matrix into sparse matrix
    sparse_matrix = to_sparse_matrix(matrix)

    # Display the sparse matrix
    display_sparse_matrix(sparse_matrix)


# Call main
if __name__ == "__main__":
    main()
