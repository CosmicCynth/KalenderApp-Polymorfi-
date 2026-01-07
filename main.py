import pygame


# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 800))
clock = pygame.time.Clock()
running = True
klikCD = 0
klikTimer = 30 



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


# Text input'
valgteText = "nil"
text = ""

TitelInput = "Titel"




# Buttons
Buttons = []
Buttons.append(Button(100,100,200,64,"Begivenhed","kalender","begivenhed")) # X,Y, Width, Height, Text, Scene
Buttons.append(Button(200,300,100,64,"Quit app","kalender","quit"))
Buttons.append(Button(0,0,100,64,"Nisse","begivenhed","select1",False))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if Scene == "begivenhed":
                if event.key == pygame.K_BACKSPACE:
                    text = TitelInput[0:-1]
                else:
                    text += event.unicode
    # Updating mouse position
    mousePos = pygame.mouse.get_pos()
    # Klik timer
    if klikCD != klikTimer:
        print(klikCD)
    if klikCD < klikTimer:
        klikCD += 1

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    if Scene == "kalender":
        screen.blit(kalenderBG, (0, 0))
    elif Scene == "begivenhed":
        print(valgteText)
        if valgteText == "Titel":
            TitelInput = text


        text_surface = text_font.render(TitelInput,True,(255,255,255))
        screen.blit(text_surface,(0,0)) # Position








    for button in Buttons:
        if button.scene == Scene: # Checker hvis knappens navn er lig med scene variablen
            if button.visible == True:
                pygame.draw.rect(screen,button.colors,(button.x,button.y,button.width,button.height)) # Tegner knappen
                button.draw_text(screen, text_font, button.textColor) # Tegner teksten til skærmen

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and klikCD >= klikTimer:
                klikCD = 0

                if button.is_clicked() == "begivenhed":
                    Scene = button.id
                elif button.is_clicked() == "select1":
                    text = ""
                    valgteText = "Titel"












    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()