import pygame
from constants import *

def get_player_name(screen):
    """Função que exibe a tela inicial e captura o nome do jogador."""
    font = pygame.font.Font(None, 48)
    input_box = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 32, 200, 64)
    color_active = pygame.Color('white')
    color_inactive = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Ativa a caixa de entrada se o jogador clicar nela
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        # Quando o jogador pressiona Enter, finaliza a entrada de texto
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        # Remove o último caractere
                        text = text[:-1]
                    else:
                        # Adiciona o caractere à string do nome
                        text += event.unicode

        # Desenha a tela de entrada
        screen.fill((0, 0, 0))  # Fundo preto
        txt_surface = font.render(text, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        # Exibe instruções na tela
        instructions = font.render("Digite seu nome e pressione Enter:", True, (255, 255, 255))
        screen.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        pygame.display.flip()

    pygame.event.clear()

    return text  # Retorna o nome do jogador
