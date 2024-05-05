class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for x in range(n)] for y in range(n)]

    def is_safe(self, row, col):
        # Check row on left side
        for i in range(col):
            if self.board[row][i]:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j]:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j]:
                return False

        return True

    def solve(self, col):
        # Base case: If all queens are placed then return True
        if col == self.n:
            return True

        # Try placing this queen in all rows one by one
        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1

                # Recur to place rest of the queens
                if self.solve(col+1):
                    return True

                # If placing queen in board[row][col] doesn't lead to a solution
                # then remove queen from board[row][col]
                self.board[row][col] = 0

        # If queen can't be placed in any row in this column col, then return False
        return False

    def print_solution(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()

# Example usage:
n = 8
nq = NQueens(n)
if nq.solve(0):
    nq.print_solution()
else:
    print(f"No solution exists for {n}x{n} board.")