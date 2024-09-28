from constants import *

import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        
    def add_points(self, points):
        self.score += points

    def get_score(self):
        return self.score

    def update(self):
        """Atualiza a imagem do score quando o valor do score muda"""
        self.image = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, 50))

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))  # Position it in the top-left corner




