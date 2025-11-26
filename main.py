# Example file showing a basic pygame "game loop"
import pygame
import interface
from interface import Button

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Kalender App")

# Buttons
Button1 = Button(100,100,50,50)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pygame.draw.rect(screen,Button1.colors,(Button1.x,Button1.y,Button1.width,Button1.height)) # Surface = screen, color, position, dimensions

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()