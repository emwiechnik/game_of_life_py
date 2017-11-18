import random 

class GameOfLife:
    def __init__(self, field_size):
        self.X = self.Y = 10
        self.board = [[0,] * self.Y for _ in range (self.X)]
        self.board2 = [[0,] * self.Y for _ in range (self.X)]
        self.field_size = field_size

    def init_board(self, count):
        for i in range (count):
            x = random.randint(0, self.X-1)
            y = random.randint(0, self.Y-1)
            self.board[x][y] = 1

    def count_neighbours(self, x, y):
        xb, yb, xe, ye = max(x-1, 0), max(y-1, 0), min(x+1, self.X-1), min(y+1, self.Y-1)
        total = 0
        for i in range(xb, xe+1):
            total += sum(self.board[i][yb:ye+1])
        return total - self.board[x][y]

    def apply_rules(self, x, y):
        n_c = self.count_neighbours(x, y)
        self.board2[x][y] = int(((self.board[x][y] == 1) and n_c in (2,3)) or ((self.board[x][y] == 0) and n_c == 3))

    def apply_rules_on_all(self):
        for x in range(self.X):
            for y in range(self.Y):
                self.apply_rules(x, y)

    def display(self):
        print()
        for line in self.board:
            print(" ".join(str(_) for _ in line))
    
    def evolve(self, n):
        self.init_board(20)
        for it in range(n):
            self.apply_rules_on_all()
            self.board, self.board2 = self.board2, self.board
            self.display()

game = GameOfLife(10)

game.evolve(5)