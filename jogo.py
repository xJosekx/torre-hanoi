import tkinter as tk
from tkinter import messagebox


class HanoiGameGUI:
    def __init__(self, num_blocks):
        self.num_blocks = num_blocks
        self.towers = {'A': [], 'B': [], 'C': []}
        self.moves = 0
        self.selected_tower = None

        self.root = tk.Tk()
        self.root.title("Jogo da Torre de Hanói")
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.initialize_game()
        self.draw_towers()

        self.canvas.bind('<Button-1>', self.on_click)

    def initialize_game(self):
        colors = ['red', 'green', 'blue', 'yellow', 'orange']  # Adicione mais cores, se desejar

        for i in range(self.num_blocks, 0, -1):
            self.towers['A'].append(colors[i - 1])

    def on_click(self, event):
        x, y = event.x, event.y
        tower_clicked = None

        if 50 <= x <= 150:
            tower_clicked = 'A'
        elif 250 <= x <= 350:
            tower_clicked = 'B'
        elif 450 <= x <= 550:
            tower_clicked = 'C'

        if tower_clicked:
            if self.selected_tower is None:
                if self.towers[tower_clicked]:
                    self.selected_tower = tower_clicked
                self.draw_towers()
            else:
                if self.selected_tower != tower_clicked and (not self.towers[tower_clicked] or self.towers[tower_clicked][-1] > self.towers[self.selected_tower][-1]):
                    self.towers[tower_clicked].append(self.towers[self.selected_tower].pop())
                    self.moves += 1
                self.selected_tower = None
                self.draw_towers()

                # Verificar se o jogo foi ganho
                if len(self.towers['B']) == self.num_blocks or len(self.towers['C']) == self.num_blocks:
                    messagebox.showinfo("Parabéns!", "Você ganhou o jogo em {} movimentos!".format(self.moves))

    def draw_towers(self):
        self.canvas.delete('all')

        tower_width = 100
        tower_height = 300

        for i, tower in enumerate(['A', 'B', 'C']):
            x = i * 200 + 100
            y = self.canvas.winfo_height() - tower_height

            self.canvas.create_rectangle(x - tower_width / 2, y, x + tower_width / 2, y + tower_height, fill='black')

            button_x = x - tower_width / 2
            button_y = y - 30
            button_width = tower_width
            button_height = 20

            self.canvas.create_rectangle(button_x, button_y, button_x + button_width, button_y + button_height,
                                         fill='light gray')

            if self.selected_tower == tower:
                self.canvas.create_text(x, button_y + button_height / 2, text="Selecionado", fill='black')
            else:
                self.canvas.create_text(x, button_y + button_height / 2, text="Selecionar", fill='black')

            tower_blocks = self.towers[tower]
            num_blocks = len(tower_blocks)

            for j, block_color in enumerate(tower_blocks):
                block_width = tower_width - (j * 10)
                block_height = tower_height / self.num_blocks

                block_x = x - block_width / 2
                block_y = y + (num_blocks - j - 1) * block_height

                self.canvas.create_rectangle(block_x, block_y, block_x + block_width, block_y + block_height,
                                             fill=block_color)

    def run(self):
        self.root.mainloop()


def main():
    num_blocks = int(input("Digite o número de blocos: "))

    game = HanoiGameGUI(num_blocks)
    game.run()


if __name__ == '__main__':
    main()
