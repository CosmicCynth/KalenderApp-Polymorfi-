import pygame
from interface import Button

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


pygame.display.set_caption("Kalender App")
text_font = pygame.font.SysFont("Arial", 24)
# Buttons
Buttons = []
Buttons.append(Button(100,100,200,64,"Begivenhed"))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    for button in Buttons:
        pygame.draw.rect(screen,button.colors,(button.x,button.y,button.width,button.height))
        button.draw_text(screen, text_font, button.textColor)



    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()