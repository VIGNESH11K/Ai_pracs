#include <stdio.h>
#include <stdbool.h>

#define ROWS 3
#define COLS 3

// Define a struct to represent the puzzle state
typedef struct {
    int grid[ROWS][COLS];
} PuzzleState;

// Function to perform depth-first search
PuzzleState dfs(PuzzleState route, int depth, PuzzleState goal) {
    // Implementation of DFS goes here
}

int main() {
    // Input initial state
    PuzzleState puzzle;
    printf("Enter initial state:\n");
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            scanf("%d", &puzzle.grid[i][j]);
        }
    }

    // Input goal state
    PuzzleState goal;
    printf("Enter goal state:\n");
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            scanf("%d", &goal.grid[i][j]);
        }
    }

    // Solve the puzzle
    PuzzleState solution = dfs(puzzle, 0, goal);

    // Print solution
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%d ", solution.grid[i][j]);
        }
        printf("\n");
    }

    return 0;
}

    