import random

HUMAN = "O"
MACHINE = "X"
board = ["1","2","3","4","X","6","7","8","9"]

def display_board():
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
    

def check_winner(player):
    return ((board[0] == board[1] == board[2] == player) or
            (board[3] == board[4] == board[5] == player) or
            (board[6] == board[7] == board[8] == player) or
            (board[0] == board[3] == board[6] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[0] == board[4] == board[8] == player) or
            (board[2] == board[4] == board[6] == player))
    
def is_board_full():
    return len(board) == board.count('X') + board.count('O')

def play_machine():
    zone = random.randint(1,9)
    if board[zone-1] == "X" or board[zone-1] == "O":
        play_machine()
    board[zone-1] = MACHINE

def play_game():
    display_board()
    print("Introduce una casilla para jugar")
    zone = int(input())

    if zone < 1 or zone > 9:
        print("Número incorrecto, inténtalo de nuevo")
        play_game()

    if board[zone-1] == "X" or board[zone-1] == "O":
        print("La casilla ya está ocupada, inténtalo de nuevo")
        play_game()

    board[zone-1] = HUMAN

    if check_winner(HUMAN) == True:
        display_board()
        print("Has ganado!")
        return
    
    play_machine()

    if check_winner(MACHINE) == True:
        display_board()
        print("Has perdido!")
        return
    
    if is_board_full == True:
        display_board()
        print("Empate!")
        return
    play_game()

def main():
    print("Bienvenido a 3 en raya:")
    play_game()
  
if __name__ == "__main__":
    main()
