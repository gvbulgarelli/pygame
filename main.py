import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    print(f"Starting pygame!")

    #initializing pygame    
    pygame.init()

    #game variables
    Clock = pygame.time.Clock()
    dt = 0
    screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    #creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #adding player to groups
    Player.containers = (updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #game loop
    while True:
    
        #checks if the window got closed and stop the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #creates the black screen with the size of screen variable
        pygame.Surface.fill(screen, "black")
        
        #update every elem position in updatable group 
        for elem in updatable:
            elem.update(dt)
        #display every elem in drawable group
        for elem in drawable:
            elem.draw(screen)
        
    #updates the screen
        pygame.display.flip()


        #clock that controls time
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()