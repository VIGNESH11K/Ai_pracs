from collections import deque

def hanoi_bfs(n):
    initial_state = ([i for i in range(n, 0, -1)], [], [])
    goal_state = ([], [], [i for i in range(n, 0, -1)])
    
    queue = deque([(initial_state, [])])
    
    while queue:
        state, moves = queue.popleft()
        if state == goal_state:
            return moves
        for i in range(3):
            for j in range(3):
                if i != j:
                    if not state[i]:
                        continue  # Skip if source tower is empty
                    elif not state[j] or state[j][-1] > state[i][-1]:
                        new_state = (state[0][:], state[1][:], state[2][:])
                        new_state[j].append(new_state[i].pop())
                        queue.append((new_state, moves + [(i, j)]))
                    
# Example usage:
n = 3  # Number of disks
solution = hanoi_bfs(n)
print("Solution:", solution)