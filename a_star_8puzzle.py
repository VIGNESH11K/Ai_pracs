import heapq

def manhattan_distance(puzzle,goal):
    distance=0
    for i in range(9):
        if puzzle[i]==0 or goal[0]:
            continue
        
        
        
