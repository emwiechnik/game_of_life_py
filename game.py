import random 
import tkinter as tk

item_on_color = 'black'
item_off_color = 'white'

world_size = 100
field_size = 5

class GameOfLife:
    def __init__(self, window, canvas, field_size):
        self.X = self.Y = world_size
        self.board = [[0,] * self.Y for _ in range (self.X)]
        self.board2 = [[0,] * self.Y for _ in range (self.X)]
        self.rect_ids = [[0,] * self.Y for _ in range (self.X)]
        self.canvas = canvas
        self.window = window
        self.field_size = field_size
        self.init_board(0.5)

    def init_board(self, threshold):
        for x in range (self.X):
            for y in range (self.Y):
                self.board[x][y] = 1 if random.random() > 0.5 else 0
                color = item_on_color if self.board[x][y] == 1 else item_off_color
                self.rect_ids[x][y] = self.canvas.create_rectangle(x * self.field_size, y * self.field_size, x * self.field_size + self.field_size, y * self.field_size + self.field_size, fill = color)

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

    def display_text(self):
        print()
        for line in self.board:
            print(" ".join(str(_) for _ in line))
			
    def display(self):
        for x in range(self.X):
            for y in range(self.Y):
                color = item_on_color if self.board[x][y] == 1 else item_off_color
                self.canvas.itemconfigure(self.rect_ids[x][y], fill = color)
        self.window.update_idletasks()
    
    def evolve(self):
        self.apply_rules_on_all()
        self.board, self.board2 = self.board2, self.board
        self.display()
        self.canvas.after(20, self.evolve)

def createCanvas():
    window = tk.Tk()
    window.title("Game of life")
    canvas = tk.Canvas(window, width = world_size * field_size, height = world_size * field_size, bg = item_off_color)  
    canvas.pack()                
    return window, canvas

window, canvas = createCanvas()

game = GameOfLife(window, canvas, field_size)

game.evolve()

window.mainloop()
