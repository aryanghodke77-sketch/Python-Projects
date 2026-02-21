
def show_board(board):
    return (
        f"\n"
        f" {board[0]} | {board[1]} | {board[2]} \n"
        f"---+---+---\n"
        f" {board[3]} | {board[4]} | {board[5]} \n"
        f"---+---+---\n"
        f" {board[6]} | {board[7]} | {board[8]} \n"
    )

def guide_show_board():
    board = [" 1", "2", "3",
            " 4", "5", "6",
            " 7", "8", "9"]

    return show_board(board)

def player_selection():
    player1 = input("\nChoose 'X' or 'O': ").upper()
    while (True):
        if (player1 == "X" or player1 == "O"):
            break
        else:
            print("Invalid choice. Please choose 'X' or 'O'.")
            player1 = input("Choose 'X' or 'O': ").upper()
            
    player2 = "O" if player1 == "X" else "X"

    return player1, player2

def player_move(board, player):
    while True:
        try:
            move = int(input(f"\nPlayer {player} choose your move (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == " ":
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number from 1 to 9.")

    board[move - 1] = player

def check_game(board):
    checklist = [[0,3,6],[1,4,7],[2,5,8], 
                 [0,1,2],[3,4,5],[6,7,8], 
                 [0,4,8],[2,4,6]]
    
    for i in checklist:
        if((board[i[0]] == board[i[1]] == board[i[2]]) and board[i[0]] != " "):
            print("The Winner is",board[i[1]])
            return 1
    
    if(" " not in board):
        print("--- TIE ----")
        return 1

    return 0

def play_again_answer(answer: str) -> bool:
    return answer.lower().startswith("y")
    
while(True):
    print("------ This is TIC TAC TOE Game ------\n")
    print(guide_show_board())
    print("\n")
    board = [" "] * 9
    print(show_board(board))
    
    player1, player2 = player_selection()
    current_player = player1
    
    while(True):
    
        player_move(board,current_player)
        print("\n",show_board(board))
        if check_game(board):
            break
        current_player = player2 if current_player == player1 else player1

    answer = input("\nDo you want to play again? (y/n): ")
    if play_again_answer(answer):
        continue
    else:
        print("\n ----- Have a nice day!!! -----")
        break