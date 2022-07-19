import chess
from MiniMax import minimax

board = chess.Board()

MAX, MIN = 100000, -100000
depth=5
pause=False

def game_not_over(board):
    i = False
    if (board.is_fivefold_repetition()):
        print("Draw by repetition")
        i = True
    if board.is_seventyfive_moves():
        print("Draw by 75 move rule")
        i = True
    if board.is_stalemate():
        print("Draw by stalemate")
        i = True
    if board.is_checkmate():
        print("Checkmate")
        i = True
    if i:
        return False
    else:
        return True


def is_legal_move(player_move):
    for i in board.legal_moves:
        legal_move=str(i)
        if(player_move==legal_move):
            return True
    print("illegal move try again")
    return False

player_color=input("Welcome to chessy chess engine choose (W)hite or (B)lack pieces ")

while (not((player_color.upper() == "B") or (player_color.upper() == "W"))):
        player_color=input("invalid input try again, press B or W ")


if player_color.upper()=="W":
    computer_moves_after=True
else:
    computer_moves_after=False


print(board)
print("play your moves so that they include coordinates of begging and ending square, for example e2e4")

while(game_not_over(board)):
    if computer_moves_after:
        player_move=input("Play your move ")
        if (is_legal_move(player_move)):
            board.push_san(player_move)
            print("you have played move")
            pause=False
        else:pause=True

    if(not pause):

        computer_move = str(minimax(depth, True, MIN, MAX, board, True))
        board.push_san(computer_move)
        print(f"Computer plays {computer_move}")
        computer_moves_after=True
        print(board)

print (board)
