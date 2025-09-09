import random

def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]
    if " " not in board:
        return "Tie"
    return None

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def computer_move(board):
    empty_spots = [i for i, spot in enumerate(board) if spot == " "]
    
    # Try winning move
    for spot in empty_spots:
        board_copy = board.copy()
        board_copy[spot] = "O"
        if check_winner(board_copy) == "O":
            return spot
    
    # Try blocking move
    for spot in empty_spots:
        board_copy = board.copy()
        board_copy[spot] = "X"
        if check_winner(board_copy) == "X":
            return spot
    
    # Choose center if available
    if 4 in empty_spots:
        return 4
    
    # Otherwise random
    return random.choice(empty_spots)

def play_game():
    board = [" "] * 9
    current_player = "X"  # Player is X, Computer is O
    
    while True:
        print_board(board)
        
        if current_player == "X":
            move = player_move(board)
        else:
            move = computer_move(board)
        
        board[move] = current_player
        result = check_winner(board)
        
        if result:
            print_board(board)
            if result == "Tie":
                print("It is a tie!")
            elif result == "X":
                print("Congratulations! You win!")
            else:
                print("Computer wins!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
