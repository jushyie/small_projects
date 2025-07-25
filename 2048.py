import random
import copy

class Board:
    def __init__(self, size = 4):
        self.size = size
        self.minimum = 2
        self.board = self.make_board()

        self.add_two()
    
    def make_board(self):
        board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        return board

    def add_two(self):
        # if the square is empty, add the number square
        while True:
            r = random.randint(0, 3)
            c = random.randint(0, 3)
            if self.board[r][c] != " ":
                continue
            else:
                self.board[r][c] = self.minimum
                return
        

    def make_move(self, move):
        # swipe up, down, left or right if there is an empty square in that direction
        if move == "u":
            self.swipe_up()
        elif move == "d":
            self.swipe_down()
        elif move == "l":
            self.swipe_left()
        elif move == "r":
            self.swipe_right()
        
        else:
            print("Invalid Input.")

    def swipe_up(self):
        # if above at least one number square is an empty spot, move all up
        for c in range(self.size):
            # add all numbers that occur in the column to a list
            num_cells = [self.board[r][c] for r in range(self.size) if self.board[r][c] != " "] 

            for r in range(self.size):

                # if two same numbers then add together
                if len(num_cells[r:]) > 1:
                    if num_cells[r] == num_cells[r+1]:
                        num_cells[r] *= 2
                        num_cells.pop(r + 1)

                # if there are numbered cells in the column, move the numbers from top to bottom upwards
                self.board[r][c] = num_cells[r] if r < len(num_cells) else " "
                                    
    def swipe_down(self):
        for c in range(self.size):
            num_cells = [self.board[r][c] for r in range(self.size) if self.board[r][c] != " "]

            for r in range(self.size - 1, -1, -1):
                idx = self.size - 1 - r

                if idx < len(num_cells) - 1:
                    if num_cells[-(idx+1)] == num_cells[-(idx+2)]:
                        num_cells[-(idx+1)] *= 2
                        num_cells.pop(-(idx+2))
                                # access the numlist from the back (reversed)
                self.board[r][c] = num_cells[-(idx + 1)] if idx < len(num_cells) else " "

    def swipe_left(self):
        for r in range(self.size):
            num_cells = [self.board[r][c] for c in range(self.size) if self.board[r][c] != " "]

            for c in range(self.size):

                if len(num_cells[c:]) > 1:
                    if num_cells[c] == num_cells[c+1]:
                        num_cells[c] *= 2
                        num_cells.pop(c + 1)

                self.board[r][c] = num_cells[c] if c < len(num_cells) else " "

    def swipe_right(self):
        for r in range(self.size):
            num_cells = [self.board[r][c] for c in range(self.size) if self.board[r][c] != " "]
            for c in range(self.size - 1, -1, -1):
                idx = self.size - 1 - c

                if idx < len(num_cells) - 1:
                    if num_cells[-(idx+1)] == num_cells[-(idx+2)]:
                        num_cells[-(idx+1)] *= 2
                        num_cells.pop(-(idx+2))

                self.board[r][c] = num_cells[-(idx + 1)] if idx < len(num_cells) else " "

    def moves_possible(self):
        for r in range(self.size):
            for c in range(self.size):
                nbrs = []

                if r > 0:
                    nbrs.append(self.board[r-1][c])
                if r < self.size - 1:
                    nbrs.append(self.board[r+1][c])
                if c > 0:
                    nbrs.append(self.board[r][c-1])
                if c < self.size - 1:
                    nbrs.append(self.board[r][c+1])
                if self.board[r][c] in nbrs:
                    return True
        return False
    


def play():
    board = Board()
    for row in board.board:
            print(row)

    empty_squares = True
    quit_game = False

    while empty_squares:
        # if condition when all squares are filled AND no more moves possible to quit game
        if all(board.board[r][c] != " " for r in range(board.size) for c in range(board.size)):
            empty_squares = board.moves_possible()
            if not empty_squares:
                print("Game Over.")
                break

        # win condition
        if any(2048 in board.board[r] for r in range(board.size)):
            print("\nYou've won the game!")
            break        

        # make sure move is possible in the specified direction
        dummy = copy.deepcopy(board.board) # before move
        while True:
            move = input("Swipe (u, d, l, r) or (q) to quit: ").lower().strip()

            if move == "q":
                quit_game = True
                break

            board.make_move(move)
            if dummy != board.board: # if the board changed
                break
            print("No move possible in that direction.")

        if quit_game:
            print("Thanks for playing.")
            break

        # with every valid move, add a new square 
        board.add_two()
        for row in board.board:
            print(row)
    
    

play()