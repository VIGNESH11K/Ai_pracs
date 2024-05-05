from collections import deque

def hanoi_bfs(n, source, target, aux):
    # Define the queue for BFS algorithm
    queue = deque()
    # Enqueue the initial state
    queue.append((n, source, target, aux))
    # Loop until the queue is empty
    while queue:
        # Dequeue the front state
        state = queue.popleft()
        # If n is 1, move the disk directly from source to target
        if state[0] == 1:
            print(f"Move disk 1 from {state[1]} to {state[2]}")
        else:
            # Enqueue the subproblems
            queue.append((state[0]-1, state[1], state[3], state[2]))
            queue.append((1, state[1], state[2], state[3]))
            queue.append((state[0]-1, state[3], state[2], state[1]))
    print("Tower of Hanoi problem solved!")

# Take user input for the number of disks and the towers
n = int(input("Enter the number of disks (min 3): "))
source = input("Enter the source tower (A, B, or C): ").upper()
target = input("Enter the target tower (A, B, or C): ").upper()
aux = input("Enter the auxiliary tower (A, B, or C): ").upper()

# Test the function with user input
hanoi_bfs(n, source, target, aux)
