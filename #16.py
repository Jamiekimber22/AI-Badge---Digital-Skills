import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence

class TicTacToe:
    BUTTON_STYLE = "Transparent.TButton"
    RESET_BUTTON_STYLE = {"font": 'normal 20 bold', "bg": 'red', "fg": 'white'}
    TURN_LABEL_STYLE = {"font": 'normal 20 bold', "bg": 'lightblue'}
    DEFAULT_BUTTON_COLOR = 'white'
    DEFAULT_BUTTON_TEXT_COLOR = 'black'

    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("640x640")
        self.create_background()
        self.player = 'X'
        self.board = [None] * 9
        self.turn_label = tk.Label(root, text="Player 1's Turn (X)", **self.TURN_LABEL_STYLE)
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Configure button style
        style = ttk.Style()
        style.configure(self.BUTTON_STYLE, background=self.DEFAULT_BUTTON_COLOR, foreground=self.DEFAULT_BUTTON_TEXT_COLOR, relief="flat")
        style.map(self.BUTTON_STYLE,
                  background=[('active', self.DEFAULT_BUTTON_COLOR)],
                  foreground=[('active', self.DEFAULT_BUTTON_TEXT_COLOR)],
                  relief=[('pressed', 'flat')],
                  highlightthickness=[('!focus', 0)],
                  focuscolor=[('!focus', self.DEFAULT_BUTTON_COLOR)])

        self.buttons = [ttk.Button(root, text='', style=self.BUTTON_STYLE, command=lambda i=i: self.click(i)) for i in range(9)]
        self.reset_button = tk.Button(root, text='Reset', command=self.reset, **self.RESET_BUTTON_STYLE)
        self.create_board()

        self.blink_count = 0  # Initialize blink_count

    def create_background(self):
        self.canvas = tk.Canvas(self.root, width=640, height=640)
        self.bg_image = Image.open("853d5b1750.gif")
        self.bg_frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(self.bg_image)]
        self.canvas.create_image(0, 0, image=self.bg_frames[0], anchor='nw')
        self.canvas.grid(row=1, column=0, columnspan=3)

    def create_board(self):
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row+2, column=col, sticky='nsew')
        self.reset_button.grid(row=5, column=0, columnspan=3, sticky='nsew')

    def click(self, index):
        if self.board[index] is None:
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.player} wins!")
                self.reset()
            elif all(self.board):
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset()
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                self.turn_label.config(text=f"Player {1 if self.player == 'X' else 2}'s Turn ({self.player})")

    def blink_winner(self):
        new_color = 'yellow' if self.blink_count % 2 == 0 else self.DEFAULT_BUTTON_COLOR
        for button in self.buttons:
            button.config(bg=new_color)
        self.blink_count += 1
        self.root.after(300, self.blink_winner)

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state='disabled')

    def reset(self):
        self.player = 'X'
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text='', state='normal', bg=self.DEFAULT_BUTTON_COLOR, fg=self.DEFAULT_BUTTON_TEXT_COLOR)
        self.turn_label.config(text="Player 1's Turn (X)")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()