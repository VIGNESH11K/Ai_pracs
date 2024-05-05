def print_board():
    print(' ', board[0], ' | ', board[1], ' | ', board[2])
    print('-----------------------')
    print(' ', board[3], ' | ', board[4], ' | ', board[5])
    print('-----------------------')
    print(' ', board[6], ' | ', board[7], ' | ', board[8])

def is_victory(player):
    victory_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for condition in victory_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw():
    return all(square != ' ' for square in board)

def player_move(player):
    while True:
        move = int(input(f"Where would you like to place your {player} (1-9)? "))
        if move < 1 or move > 9:
            print("Invalid move.")
        elif board[move - 1] != ' ':
            print("That square is already occupied.")
        else:
            board[move - 1] = player
            break

def ai_move(player):
    magic_square = [4, 9, 2, 7, 5, 3, 6, 1, 8]
    for i, square in enumerate(magic_square):
        if board[square - 1] == ' ':
            board[square - 1] = player
            break

board = [' ' for i in range(9)]

def main():
    while True:
        print_board()
        player_move('X')
        print_board()
        if is_victory('X'):
            print("X wins! Congratulations!")
            break
        elif is_draw():
            print("It's a draw!")
            break
        ai_move('O')
        if is_victory('O'):
            print_board()
            print("O wins! Better luck next time.")
            break
        elif is_draw():
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()