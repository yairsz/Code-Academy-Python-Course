from random import randint


class Ship(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def is_on_coord(self, x, y):
        if x == self.row & y == self.col:
            return True
        else:
            return False


class Game(object):
    board = []
    ships = []

    def __init__(self, size, n_of_ships):
        for x in range(size):
            self.board.append(["O"] * size)
            self.size = size
        for i in range(n_of_ships):
            self.add_ship()

    def print_board(self):
        for row in self.board:
            print " ".join(row)

    def add_ship(self):
        was_added = False
        while not was_added:
            new_ship = Ship(randint(0, self.size), randint(0, self.size))
            if len(self.ships) == 0:
                self.ships.append(new_ship)
                was_added = True
            elif len(self.ships) > 0:
                for ship in self.ships:
                    if ship.is_on_coord(new_ship.row, new_ship.col):
                        break
                else:
                    self.ships.append(new_ship)
                    was_added = True

    def is_hit(self, row, col):
        hit = False
        for ship in self.ships:
            if ship.is_on_coord(row, col):
                hit = True
                break
        return hit



game = Game(5, 6)

print "Let's play Battleship!"
game.print_board()

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):

    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if game.is_hit(guess_row, guess_col):
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row > game.size) or (guess_col > game.size) or (guess_row < 0) or (guess_col < 0):
            print "Oops, that's not even in the ocean."
        elif game.board[guess_row-1][guess_col-1] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            game.board[guess_row-1][guess_col-1] = "X"
            if turn >= 3:
                print "Game Over"

    # Print (turn + 1) here!
        print (turn + 1)
        game.print_board()
