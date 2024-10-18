# Copilot

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.player = 'X'
        self.board = [None] * 9
        self.buttons = [tk.Button(root, text='', font='normal 20 bold', width=5, height=2, command=lambda i=i: self.click(i)) for i in range(9)]
        self.reset_button = tk.Button(root, text='Reset', font='normal 20 bold', command=self.reset)
        self.create_board()

    def create_board(self):
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def click(self, index):
        if self.board[index] is None:
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.player} wins!")
                self.disable_buttons()
            elif None not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] is not None:
                return True
        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state='disabled')

    def reset(self):
        self.player = 'X'
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text='', state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()