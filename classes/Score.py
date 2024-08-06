import pygame as pg

class Score:
    def __init__(self):
        self.score = 0

    def change_score(self, points):
        self.score += points

    # Отрисовка очков
    def draw_score(self, screen, glass, color):
        font = pg.font.Font(None, 36)

        text = font.render("Score: " + str(self.score), True, color)
        screen.blit(text, (glass.size_cell * glass.width_cell_amount + (screen.get_width() - glass.size_cell * glass.width_cell_amount) // 2, 10))