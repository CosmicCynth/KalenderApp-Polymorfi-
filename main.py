import pygame


# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 800))
clock = pygame.time.Clock()
running = True


# App setup
global Scene
Scene = "kalender"

global mousePos
mousePos = pygame.mouse.get_pos()

#Modules
from interface import Button

#Sprites
kalenderBG = pygame.image.load("sprites/kalenderbg.png").convert()

pygame.display.set_caption("Kalender App")
text_font = pygame.font.SysFont("Arial", 24)
# Buttons
Buttons = []
Buttons.append(Button(100,100,200,64,"Begivenhed","kalender","labubu")) # X,Y, Width, Height, Text, Scene
Buttons.append(Button(200,300,100,64,"Quit app","kalender","quit"))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Updating mouse position
    mousePos = pygame.mouse.get_pos()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    if Scene == "kalender":
        screen.blit(kalenderBG, (0, 0))


    for button in Buttons: # Looper igennem alle knapper
        if button.scene == Scene: # Checker hvis knappens navn er lig med scene variablen
            pygame.draw.rect(screen,button.colors,(button.x,button.y,button.width,button.height)) # Tegner knappen
            button.draw_text(screen, text_font, button.textColor) # Tegner teksten til skærmen

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.is_clicked():
                    Scene = button.is_clicked()









    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()