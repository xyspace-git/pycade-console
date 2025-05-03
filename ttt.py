'''
DOCUMENTATION
Created by @aftonsenpai - 05:23 AM | 19/12/24
Last Updated: 02:11 AM | 04/05/25
Type - Console Game
Title - Tic-Tac-Toe
Version - 2.0.0
'''

# ======================= #
#    TIC TAC TOE GAME     #
# ======================= #

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if move not in range(9):
                print("Invalid input. Choose from 1 to 9.")
            elif board[row][col] in ['X', 'O']:
                print("Cell already taken. Choose another.")
            else:
                return row, col
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

def main():
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    current_player = 'X'
    
    print("Welcome to Pycade Console - Tic Tac Toe\n")
    print_board(board)
    
    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins! 🎉")
            break
        elif is_full(board):
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
