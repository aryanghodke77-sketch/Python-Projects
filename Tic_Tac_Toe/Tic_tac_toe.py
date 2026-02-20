
def guide_show():
    board = [" 1", "2", "3",
            " 4", "5", "6",
            " 7", "8", "9"]

    print(board[0], "|", board[1], "|", board[2])
    print("-----------")
    print(board[3], "|", board[4], "|", board[5])
    print("-----------")
    print(board[6], "|", board[7], "|", board[8])

def show(board):

    print(board[0], " |", board[1], "|", board[2])
    print("-----------")
    print(board[3], " |", board[4], "|", board[5])
    print("-----------")
    print(board[6], " |", board[7], "|", board[8])

def player_selection():
    player1 = input("\nChoose 'X' or 'O': ").upper()
    while (True):
        if (player1 == "X" or player1 == "O"):
            break
        else:
            print("Invalid choise. Please choose 'X' or 'O'.")
            player1 = input("Choose 'X' or 'O': ").upper()
            
    player2 = "O" if player1 == "X" else "X"

    return player1, player2

def player_move(board,player):
    move = int(input(f"\nPlayer {player} choose your move (1-9): "))
    while not (1 <= move <= 9) or (board[move - 1] != " "):
        move = int(input(f"Invalide choice. Player {player} choose your move (1-9): "))

    board[move - 1] = player
    show(board)

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
    
def game():
    print("------ This is TIC TAC TOE Game ------\n")
    guide_show()
    print("\n")
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    show(board)
    
    player1, player2 = player_selection()
    current_player = player1
    
    while(True):
    
        player_move(board,current_player)
        if check_game(board):
            break
        current_player = player2 if current_player == player1 else player1

    a = input("Want to play again (y/n) : ")

    if a == "y":
        game()
    else:
        print("\n ----- Have a nice day!!! -----")

game()