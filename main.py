import pygame

from begivenheder import nyBegivenhed

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 800))
clock = pygame.time.Clock()
running = True
klikCD = 0 # Timer
klikTimer = 30 # Tiden inden brugeren må klikke som er et halv sek



# App setup
global Scene
Scene = "kalender"

global mousePos
mousePos = pygame.mouse.get_pos()

#Modules
from interface import Button
import begivenheder
from begivenheder import nyBegivenhed



#Sprites
kalenderBG = pygame.image.load("sprites/kalenderbg.png").convert()

pygame.display.set_caption("Kalender App")
text_font = pygame.font.SysFont("Arial", 24)


# Text input'
valgteText = "nil"
text = ""

TitelInput = "Titel"
KategoriInput = "Kategori"
TidspunktInput = "Tidspunkt"




# Buttons
Buttons = []
Buttons.append(Button(100,100,200,64,"Begivenhed","kalender","begivenhed")) # X,Y, Width, Height, Text, Scene
Buttons.append(Button(200,300,100,64,"Quit app","kalender","quit"))
Buttons.append(Button(0,0,100,64,"Nisse","begivenhed","selectTitel",False))
Buttons.append(Button(2,100,99,32,"Work please","begivenhed","selectKategori",False))
Buttons.append(Button(2,200,99,32,"Work please1","begivenhed","selectTidspunkt",False))
Buttons.append(Button(2,300,99,32,"Færdig?","begivenhed","LavBegivenhed",True))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if Scene == "begivenhed":
                if event.key == pygame.K_BACKSPACE:
                    text = text[0:-1]
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    valgteText = "nil"
                else:
                    text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and klikCD >= klikCD:
            klikCD = 0
            pos = event.pos

            for button in Buttons:
                if button.scene == Scene:
                    if button.is_clicked(pos):
                        if button.id == "begivenhed":
                            Scene = "begivenhed"
                        elif button.id == "selectTitel":
                            text = ""
                            valgteText = "Titel"
                        elif button.id == "selectKategori":
                            text = ""
                            valgteText = "Kategori"
                        elif button.id == "selectTidspunkt":
                            text = ""
                            valgteText = "Tidspunkt"
                        elif button.id == "LavBegivenhed":
                            nyBegivenhed(TitelInput,KategoriInput,"24 Juli 2067",TidspunktInput)
                        else:
                            print("Clicked:", button.id)



    # Updating mouse position
    mousePos = pygame.mouse.get_pos()
    # Klik timer
    #if klikCD != klikTimer:
        #print(klikCD)
    if klikCD < klikTimer:
        klikCD += 1

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    if Scene == "kalender":
        screen.blit(kalenderBG, (0, 0))
    elif Scene == "begivenhed":
        #print(valgteText)
        if valgteText == "Titel":
            TitelInput = text
        elif valgteText == "Kategori":
            KategoriInput = text
        elif valgteText == "Tidspunkt":
            TidspunktInput = text


        title_surface = text_font.render(TitelInput,True,(255,255,255))
        screen.blit(title_surface,(0,0)) # Position

        kategori_surface = text_font.render(KategoriInput,True,(255,255,255))
        screen.blit(kategori_surface,(0,100)) # Position

        tidspunkt_surface = text_font.render(TidspunktInput, True, (255, 255, 255))
        screen.blit(tidspunkt_surface, (0, 200))  # Position








    for button in Buttons:
        if button.scene == Scene: # Checker hvis knappens navn er lig med scene variablen
            if button.visible == True:
                pygame.draw.rect(screen,button.colors,(button.x,button.y,button.width,button.height)) # Tegner knappen
                button.draw_text(screen, text_font, button.textColor) # Tegner teksten til skærmen













    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()