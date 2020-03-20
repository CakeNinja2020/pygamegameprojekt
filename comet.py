import pygame


class comet_class:
    x = 0
    y = 0
    # 166,149
    comet_count = 0

    def __init__(self, spawn_pos_X, spawn_pos_Y,comet):
        self.x = spawn_pos_X
        self.y = spawn_pos_Y
        self.comet_count = 0
        self.comet = comet

    def update(self):
        self.x -= 25
        self.y += 25

    def draw(self,screen):
        self.display = screen
        screen.blit(self.comet[self.comet_count], (self.x, self.y))
        self.comet_count += 1
        if self.comet_count >= 10:
            self.comet_count = 0
