from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))
    
    def __str__(self):
        s = ''
        for i in range(0, 9, 3):
            s += ' '.join(str(x) for x in self.state[i:i+3]) + '\n'
        return s
        
    def expand(self):
        successors = []
        for action in self.get_actions():
            new_state = self.get_result(action)
            new_node = Node(new_state, self, action, self.cost + self.get_cost(action))
            successors.append(new_node)
        return successors
    
    def get_actions(self):
        actions = []
        for i in range(len(self.state)):
            if self.state[i] == 0:
                if i % 3 != 0:
                    actions.append('left')
                if i % 3 != 2:
                    actions.append('right')
                if i >= 3:
                    actions.append('up')
                if i <= 5:
                    actions.append('down')
        return actions
    
    def get_result(self, action):
        i = self.state.index(0)
        if action == 'left' and i % 3 != 0:
            j = i - 1
        elif action == 'right' and i % 3 != 2:
            j = i + 1
        elif action == 'up' and i >= 3:
            j = i - 3
        elif action == 'down' and i <= 5:
            j = i + 3
        else:
            return None
        new_state = list(self.state)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return tuple(new_state)
    
    def get_cost(self, action):
        return 1
    
def ucs(start_state, goal_state):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, Node(start_state)))

    while not pq.empty():
        _, node = pq.get()

        if node.state == goal_state:
            path = []
            while node.parent is not None:
                path.append((node.action, node))
                node = node.parent
            path.reverse()
            return path

        if node not in visited:
            visited.add(node)

            for successor in node.expand():
                pq.put((successor.cost, successor))

    return None

start_state = (7, 2, 4, 5, 0, 6, 8, 3, 1)
goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

solution = ucs(start_state, goal_state)

if solution is None:
    print('No solution found')
else:
    for step in solution:
        print(step[1])  # prints the state of the node in the solution
        print("-----")  # prints an empty line for spacing