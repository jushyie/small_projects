import random

class Board:
    def __init__(self):
        self.board = [(["_"] * 3) for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print("|".join(row))

    def player_move(self):
        column = int(input("Column (1-3): ")) - 1
        row = int(input("Row (1-3): ")) - 1
        print()
        if self.board[column][row] == "_":
            self.board[column][row] = "X"
            return
        else:
            print("Space occupied")
            self.player_move()
        
    def computer_move(self):
        print("\nComputer move:")
        column = random.choice(range(3))
        row = random.choice(range(3))
        if self.board[column][row] == "_":
            self.board[column][row] = "O"
            return
        else:
            print("Space occupied")
            self.computer_move()
    
    def game_state(self, current):
        for i in range(3):
            if all(self.board[i][x] == current for x in range(3)):
                return True
            elif all(self.board[x][i] == current for x in range(3)):
                return True
            
        if all(self.board[x][x] == current for x in range(3)):
            return True
        elif all(self.board[2-x][x] == current for x in range(3)):
            return True
    



def main():
    board = Board()
    current = "X"
    while True:
        board.print_board()
        if current == "X":
            board.player_move()
        elif current == "O":
            board.computer_move()

        status = board.game_state(current)
        if status is True:
            board.print_board()
            print(f"{current} Player won!")
            return
        elif all("_" not in row for row in board.board):
            print("No more spaces.")
            return
        current = "X" if current != "X" else "O"

        

main()