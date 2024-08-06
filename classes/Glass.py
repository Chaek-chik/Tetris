import pygame as pg

class Glass:
    def __init__(self):
        self.width_cell_amount = 10
        self.height_cell_amount = 20
        self.size_cell = 30
    
    # Обновление сетки игрового поля
    def update_glass(self, grid, shape, x, y, color):
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] == 1:
                    grid[y + row][x + col] = color

    # Удаление заполненных линий
    def remove_lines(self, grid, glass, color, score, screen):

        full_lines = []
        for row in range(glass.height_cell_amount):
            if all(cell != color['BLACK'] for cell in grid[row]):
                full_lines.append(row)
        for row in full_lines:
            del grid[row]
            grid.insert(0, [color['BLACK']] * glass.width_cell_amount)
            score.change_score(10)
            score.draw_score(screen = screen, glass = glass, color = color['WHITE'])
    
    # Отрисовка игрового поля
    def draw_glass(self, grid, glass, screen, color):
        for row in range(glass.height_cell_amount):
            for col in range(glass.width_cell_amount):
                pg.draw.rect(screen, grid[row][col], (col * glass.size_cell, row * glass.size_cell, glass.size_cell, glass.size_cell), 1)
        pg.draw.line(screen, color['GREY'], [glass.size_cell * glass.width_cell_amount + 1, 0], [glass.size_cell * glass.width_cell_amount + 1, screen.get_height()], 1)