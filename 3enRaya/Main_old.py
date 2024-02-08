

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[0] + "   |   " + board[1] + "   |   " + board[2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[3] + "   |   " + board[4] + "   |   " + board[5] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[6] + "   |   " + board[7] + "   |   " + board[8] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    

def check_winner(board, player):
    return ((board[0] == board[1] == board[2] == player) or
            (board[3] == board[4] == board[5] == player) or
            (board[6] == board[7] == board[8] == player) or
            (board[0] == board[3] == board[6] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[0] == board[4] == board[8] == player) or
            (board[2] == board[4] == board[6] == player))

def is_board_full(board):
    return len(board) == board.count('X') + board.count('O')

def main():
    HUMAN = "O"
    MACHINE = "X"
    board = ["1","2","3","4","X","5","6","7","8","9"]

    print("Bienvenido a 3 en raya:")
    display_board(board)
    print(check_winner(board,HUMAN))


if __name__ == "__main__":
    main()
