# this allows us to use code from the open-source pygame library throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
  
    #Creating groups to manage CPU usage
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Player containers and draw
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    #Asteroid containers and draw
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    
    #Shot continer
    Shot.containers = (shots, updatable, drawable)
    
    #Delta Time Variable
    dt = 0
    
    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Functionally allows the screen to update with player input
            # Previously player.update(dt)
        for obj in updatable:
            obj.update(dt)

        #Check for collisions with player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
                
        #Check for collisions with bullets
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    


        #Fill the displayed window with the color black
        screen.fill("black")
        
        #Draw the Player on the Screen
            #Previously player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        #Limit the frame rate to 60 FPS
        # Divide by 1000 to convert from ms to s
        dt = clock.tick(60) / 1000
    
# Run main function to tell the program to actually run    
if __name__ == "__main__":
    main()
