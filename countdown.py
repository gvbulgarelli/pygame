import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def countdown(screen):
    pygame.init()
    font_large = pygame.font.Font(None, 144)
    font_small = pygame.font.Font(None, 72)
    
    countdown_time = 3  # Countdown from 3 seconds
    last_update = pygame.time.get_ticks()
    current_count = countdown_time
    
    while current_count > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((0, 0, 0))
        
        # Render the "Starting in..." text
        starting_text = font_small.render("Starting in...", True, pygame.Color('white'))
        starting_rect = starting_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100))
        screen.blit(starting_text, starting_rect)
        
        # Render the countdown number
        countdown_text = font_large.render(str(current_count), True, pygame.Color('white'))
        countdown_rect = countdown_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(countdown_text, countdown_rect)
        
        pygame.display.flip()
        
        # Update the countdown every second
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= 1000:  # 1000 milliseconds = 1 second
            current_count -= 1
            last_update = current_time

    # Clear the screen after countdown
    screen.fill((0, 0, 0))
    pygame.display.flip()