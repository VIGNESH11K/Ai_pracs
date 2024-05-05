def print_board():
    print('',board[0],|,board[1],|,board[2])
    print('',board[3],|,board[4],|,board[5])
    print('',board[6],|,board[7],|,board[8])
    
def is_victory(player):
    victory_conditions= [
        [0,1,2],[3,4,5],[6,7,8], #row
        [0,3,6],
        
    ]
    
    