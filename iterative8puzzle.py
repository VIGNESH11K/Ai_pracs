import heapq

def manhattan_distance(state):
    """
    Calculates the Manhattan distance of a given state.
    """
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                correct_i, correct_j = divmod(state[i][j] - 1, 3)
                distance += abs(i - correct_i) + abs(j - correct_j)
    return distance

class Node:
    """
    A node in the search tree.
    """
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __repr__(self):
        return f"Node({self.state}, parent={self.parent}, action={self.action}, cost={self.cost})"

    def __lt__(self, other):
        return self.cost < other.cost

def get_moves(state):
    """
    Returns a list of possible moves from a given state.
    """
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zrow, zcol = i, j
                break
    # south
    if zrow < 2:
        moves.append(swap(zrow + 1, zcol, state))
    # west
    if zcol > 0:
        moves.append(swap(zrow, zcol - 1, state))
    # north
    if zrow > 0:
        moves.append(swap(zrow - 1, zcol, state))
    # east
    if zcol < 2:
        moves.append(swap(zrow, zcol + 1, state))
    return moves

def swap(row, col, state):
    """
    Swaps the 0 with the given row and column.
    """
    new_state = [row[:] for row in state]
    zrow, zcol = 0, 0
    for i in range(3):
        for j in range(3):
            if new_state[i][j] == 0:
                zrow, zcol = i, j
                break
    new_state[zrow][zcol], new_state[row][col] = new_state[row][col], new_state[zrow][zcol]
    return new_state

def accept():
    """
    Accepts the initial and goal states from the user.
    """
    puz = []
    for i in range(3):
        temp = input().split(" ")
        temp_to_int=[int(i) for i in temp]
        puz.append(temp_to_int)
    return puz

def solve(state):
    """
    Solves the 8-puzzle problem using A* algorithm.
    """
    start_node = Node(state)
    frontier = [start_node]
    heapq.heapify(frontier)
    explored = set()
    while frontier:
        current_node = heapq.heappop(frontier)
        if current_node.state == goal_state:
            return current_node
        explored.add(tuple(map(tuple, current_node.state)))
        for move in get_moves(current_node.state):
            new_node = Node(move, current_node, current_node.action, current_node.cost + 1)
            new_node.cost += manhattan_distance(new_node.state)
            if tuple(map(tuple, new_node.state)) not in explored:
                heapq.heappush(frontier, new_node)
    return None

print("Enter initial state :")
state = accept()
print("Enter goal state :")
goal_state = accept()
solution = solve(state)
if solution is not None:
    print("Solution found!")
    while solution is not None:
        print(solution.state)
        solution = solution.parent
else:
    print("No solution found.")