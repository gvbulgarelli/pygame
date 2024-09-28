import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from lifes import LifeTracker
from menu import get_player_name

def main():
    print(f"Starting pygame!")

    #initializing pygame    
    pygame.init()
    pygame.font.init()  # Add this line

    #game variables
    Clock = pygame.time.Clock()
    dt = 0
    screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player_name = None
    first_run = True
    game_over = False

    #controla o game state para garantir que a primeira vez que o jogo carregar ele abra o menu
    game_state = "menu"

    #creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    

    #adding player to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    asterodifield = AsteroidField()

    if game_state == "menu":
        # Exibe a tela de entrada do nome e captura o nome do jogador
        player_name = get_player_name(screen)
        game_state = "playing"  # Muda o estado para o jogo principal
        player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, player_name)
        lifes = LifeTracker(player, INITIAL_LIFES)
        score = Score(player_name)
    
    

    drawable.add(score)
    drawable.add(lifes)

    

    #game loop
    while True:

        
        if game_state == "playing":
            #checks if the window got closed and stop the program
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == SCORE_CHANGE_EVENT:
                    score.add_points(event.points)
                elif event.type == pygame.KEYDOWN and game_over:
                    if event.key == pygame.K_RETURN:  # Verifica se a tecla "Enter" foi pressionada
                        game_over = False
                        player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                        asteroidfield = AsteroidField()  # Recria o campo de asteroides
                        asteroids.empty()  # Remove todos os asteroides

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Verifica se a tecla "Enter" foi pressionada
            
            if game_over:
                continue
                
            #creates the black screen with the size of screen variable
            pygame.Surface.fill(screen, "black")
            
            #update every elem position in updatable group 
            for elem in updatable:
                elem.update(dt)
            #display every elem in drawable group
            for item in asteroids:
                if item.collision(player):
                    lifes.deacrese_lifes(1)
                    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    for asteroid in asteroids:
                        asteroid.kill()
                    game_over = True
                    print("Se fudeu mané!")
                    pass
                for bullet in shots:
                    if item.collision(bullet):
                        bullet.kill()
                        item.split()
            for elem in drawable:
                elem.draw(screen)
            
        #updates the screen
            pygame.display.flip()

            #clock that controls time
            dt = Clock.tick(60) / 1000


if __name__ == "__main__":
    main()