import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    print(f"Starting pygame!")

    #initializing pygame    
    pygame.init()
    pygame.font.init()  # Add this line

    #game variables
    Clock = pygame.time.Clock()
    dt = 0
    screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

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


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asterodifield = AsteroidField()
    score = Score("Player1")

    drawable.add(score)

    #game loop
    while True:
        #checks if the window got closed and stop the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == SCORE_CHANGE_EVENT:
                score.add_points(event.points)
            
        #creates the black screen with the size of screen variable
        pygame.Surface.fill(screen, "black")
        
        #update every elem position in updatable group 
        for elem in updatable:
            elem.update(dt)
        #display every elem in drawable group
        for item in asteroids:
            if item.collision(player):
                print("Se fudeu mané!")
                return
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