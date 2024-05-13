from collections import deque

def hanoi_bfs(n,source,target,aux):
    queue =deque()
    queue.append,source,target,aux
    
    while queue:
        state=queue.popleft()
        
        if state[0]==1:
            print("move dist 1 from {state[1]} to {state[2]}")
        
        else:
            queue.append(([state[0-1]],state[1],state[3],state[2]))
            queue.append((1,state[1],state[2],state[3]))
            queue.append(([state[0-1]],state[3],state[2],state[1]))
            
        print("Tower of Hanoi solved")
        
    
    n=int(input("Enter disk min 3:"))
    source=input("Enter tower")
    target=input("enter target")
    aux=input("Enter aux")
    
    hanoi_bfs(n,source,target,aux)
            
        
              
                  
        