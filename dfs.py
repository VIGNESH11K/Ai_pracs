def hanoi_dfs(n, source, target, aux):
    # Define the stack for DFS algorithm
    stack = []
    # Push the initial state to the stack
    stack.append((n, source, target, aux))
    # Loop until the stack is empty
    while stack:
        # Pop the top state from the stack
        state = stack.pop()
        # If n is 1, move the disk directly from source to target
        if state[0] == 1:
            print(f"Move disk 1 from {state[1]} to {state[2]}")
        else:
            # Push the subproblems to the stack
            stack.append((state[0]-1, state[1], state[3], state[2]))
            stack.append((1, state[1], state[2], state[3]))
            stack.append((state[0]-1, state[3], state[2], state[1]))
    print("Tower of Hanoi problem solved!")

# Take user input for the number of disks and the towers
n = int(input("Enter the number of disks (min 3): "))
source = input("Enter the source tower (A, B, or C): ")
target = input("Enter the target tower (A, B, or C): ")
aux = input("Enter the auxiliary tower (A, B, or C): ")

# Test the function with user input
hanoi_dfs(n, source, target, aux)