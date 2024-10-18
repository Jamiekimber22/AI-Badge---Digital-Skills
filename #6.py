# GPT V3

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x450")
        self.root.configure(bg='lightblue')
        self.player = 'X'
        self.board = [None] * 9
        self.turn_label = tk.Label(root, text="Player 1's Turn (X)", font='normal 20 bold', bg='lightblue')
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=10)
        self.buttons = [tk.Button(root, text='', font='normal 20 bold', width=5, height=2, bg='white', fg='black', command=lambda i=i: self.click(i)) for i in range(9)]
        self.reset_button = tk.Button(root, text='Reset', font='normal 20 bold', bg='red', fg='white', command=self.reset)
        self.create_board()

    def create_board(self):
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row+1, column=col, padx=5, pady=5)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)

    def click(self, index):
        if self.board[index] is None:
            self.board[index] = self.player
            self.buttons[index].config(text=self.player, fg='blue' if self.player == 'X' else 'green')
            if self.check_winner():
                self.highlight_winner()
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.player} wins!")
                self.disable_buttons()
            elif None not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                self.turn_label.config(text=f"Player {'1' if self.player == 'X' else '2'}'s Turn ({self.player})")

    def check_winner(self):
        self.win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in self.win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] is not None:
                self.winning_combination = (a, b, c)
                return True
        return False

    def highlight_winner(self):
        self.blink_count = 0
        self.blink_winner()

    def blink_winner(self):
        if self.blink_count < 10:
            for index in self.winning_combination:
                current_color = self.buttons[index].cget('bg')
                new_color = 'yellow' if current_color == 'white' else 'white'
                self.buttons[index].config(bg=new_color)
            self.blink_count += 1
            self.root.after(300, self.blink_winner)

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state='disabled')

    def reset(self):
        self.player = 'X'
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text='', state='normal', bg='white', fg='black')
        self.turn_label.config(text="Player 1's Turn (X)")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()