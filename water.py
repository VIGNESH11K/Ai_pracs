from collections import deque

# Production rules
def fill_first_jug(x, y, a):
    return (a, y)

def fill_second_jug(x, y, b):
    return (x, b)

def empty_first_jug(x, y):
    return (0, y)

def empty_second_jug(x, y):
    return (x, 0)

def pour_from_second_to_first(x, y, a, b):
    return (min(x + y, a), max(0, x + y - a))

def pour_from_first_to_second(x, y, a, b):
    return (max(0, x + y - b), min(x + y, b))

# BFS function
def bfs(initial_state, goal_state, a, b):
    queue = deque([(initial_state, [initial_state])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        if state in visited:
            continue
        visited.add(state)
        x, y = state
        if x < a:
            queue.append((fill_first_jug(x, y, a), path + [fill_first_jug(x, y, a)]))
        if y < b:
            queue.append((fill_second_jug(x, y, b), path + [fill_second_jug(x, y, b)]))
        if x > 0:
            queue.append((empty_first_jug(x, y), path + [empty_first_jug(x, y)]))
        if y > 0:
            queue.append((empty_second_jug(x, y), path + [empty_second_jug(x, y)]))
        if y > 0:
            queue.append((pour_from_second_to_first(x, y, a, b), path + [pour_from_second_to_first(x, y, a, b)]))
        if x > 0:
            queue.append((pour_from_first_to_second(x, y, a, b), path + [pour_from_first_to_second(x, y, a, b)]))
    return False

# Main function
def main():
    initial_state = (0, 0)
    goal_state = (4, 0)
    a = 5
    b = 3
    result = bfs(initial_state, goal_state, a, b)
    if result:
        print("Goal state is reachable")
        print("Steps:")
        for step in result:
            print(step)
    else:
        print("Goal state is not reachable")

if __name__ == '__main__':
    main()