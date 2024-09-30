import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def show_menu(screen):
    pygame.init()
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    
    # Load game logo with error handling
    try:
        logo = pygame.image.load('logo.png')
    except pygame.error as e:
        print(f"Failed to load image: {e}")
        pygame.quit()
        sys.exit()
    
    # Resize the logo to fit within the circle
    logo_radius = int(min(SCREEN_WIDTH, SCREEN_HEIGHT) * 0.2)  # 20% of the smaller screen dimension
    logo_diameter = logo_radius * 2
    logo = pygame.transform.scale(logo, (logo_diameter, logo_diameter))
    
    # Create a circular mask
    mask_surface = pygame.Surface((logo_diameter, logo_diameter), pygame.SRCALPHA)
    pygame.draw.circle(mask_surface, (255, 255, 255, 255), (logo_radius, logo_radius), logo_radius)
    
    # Apply the mask to the logo
    logo_surface = pygame.Surface((logo_diameter, logo_diameter), pygame.SRCALPHA)
    logo_surface.blit(logo, (0, 0))
    logo_surface.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    
    logo_rect = logo_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    
    # Create text surfaces
    game_name = font.render("Asteroids", True, pygame.Color('white'))
    game_name_rect = game_name.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    
    start_button = small_font.render("Click here to Start!", True, pygame.Color('white'))
    start_button_rect = start_button.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5))
    
    player_name = ""
    input_active = False
    input_box = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 1.2, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    
    show_start_button = True
    start_button_timer = pygame.time.get_ticks()
    show_input_prompt = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    input_active = True
                    color = color_active
                    show_input_prompt = True
                elif input_box.collidepoint(event.pos):
                    input_active = True
                    color = color_active
                else:
                    input_active = False
                    color = color_inactive
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        if player_name:
                            return player_name
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode
        
        screen.fill((0, 0, 0))
        
        # Draw the circle logo
        screen.blit(logo_surface, logo_rect)
        
        screen.blit(game_name, game_name_rect)
        
        # Blink the start button
        current_time = pygame.time.get_ticks()
        if current_time - start_button_timer > 500:  # Toggle every 500ms
            show_start_button = not show_start_button
            start_button_timer = current_time
        
        if show_start_button and not show_input_prompt:
            screen.blit(start_button, start_button_rect)
        
        if show_input_prompt:
            input_prompt = small_font.render("Insert your name and press enter to start", True, pygame.Color('white'))
            input_prompt_rect = input_prompt.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5))
            screen.blit(input_prompt, input_prompt_rect)
            
            input_box.y = input_prompt_rect.bottom + 10  # Position the input box a few pixels below the prompt text
            
            txt_surface = small_font.render(player_name, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)
        
        pygame.display.flip()