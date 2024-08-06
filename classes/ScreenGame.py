import pygame as pg

class ScreenGame:
    def __init__(self):
        self.width = 800
        self.height = 600
        
        self.screen = pg.display.set_mode((self.width, self.height))
        self.caption = pg.display.set_caption('Tetris')
        