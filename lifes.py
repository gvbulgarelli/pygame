from constants import *

import pygame

class LifeTracker(pygame.sprite.Sprite):
    tracker_count = 0

    def __init__(self, player, lifes):
        super().__init__()
        self.player = player
        self.lives = lifes
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.index = LifeTracker.tracker_count
        LifeTracker.tracker_count += 1
        
    def deacrese_lifes(self, lifes):
        if self.lives > 0:
            self.lives -= lifes

    def get_lifes(self):
        return self.lifes

    def draw(self, screen):

        life_text = self.font.render(f"{self.player.name} lifes: {self.lives}", True, (255, 255, 255))


        x_position = SCREEN_WIDTH - life_text.get_width() - 20  # Alinha à direita
        y_position = 20 + self.index * (life_text.get_height() + 10)  # Posiciona abaixo conforme o índice
        screen.blit(life_text, (x_position, y_position))  # Position it in the top-left corner
