def print_board(board):
    """Prints the board in a readable format."""
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def is_safe(board, row, col, N):
    """Check if placing a queen at (row, col) is safe."""
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, N):
    """Recursive function to place queens on the board."""
    if row == N:  # If all queens are placed, return True
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place queen

            if solve_n_queens_util(board, row + 1, N):  # Recur for next row
                return True

            board[row][col] = 0  # Backtrack if no valid solution

    return False  # No valid placement for this row

def solve_n_queens(N):
    """Main function to solve N-Queens."""
    board = [[0] * N for _ in range(N)]

    if not solve_n_queens_util(board, 0, N):
        print("No solution exists.")
    else:
        print("Solution exists. Queen placements:")
        print_board(board)

# Get user input
N = int(input("Enter the number of queens: "))
solve_n_queens(N)
