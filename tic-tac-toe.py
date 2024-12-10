def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Checks if the player has won."""
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all(cell != ' ' for row in board for cell in row)

def get_move():
    """Gets the player's move and ensures it's valid."""
    while True:
        try:
            move = input("Enter your move (row and column: 1 2): ").split()
            row, col = int(move[0]) - 1, int(move[1]) - 1  # Convert to 0-based index
            if row not in range(3) or col not in range(3):
                print("Invalid move! Row and column must be between 1 and 3.")
            else:
                return row, col
        except (ValueError, IndexError):
            print("Invalid input! Please enter two numbers (row and column) separated by a space.")

def play_game():
    """Main function to play the Tic-Tac-Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 empty board
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}, it's your turn.")
        
        # Get the move from the player
        row, col = get_move()

        # Check if the chosen cell is already occupied
        if board[row][col] != ' ':
            print("This cell is already taken! Please choose another cell.")
            continue

        # Update the board with the current player's move
        board[row][col] = current_player
        print_board(board)

        # Check for a winner
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if is_board_full(board):
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
