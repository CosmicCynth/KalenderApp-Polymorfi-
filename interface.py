import pygame.mouse

class Button:
    def __init__(self, x, y, width, height, text, scene, id, visible=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.scene = scene
        self.id = id
        self.visible = visible

        self.colors = (255, 255, 255)
        self.textColor = (0,0,0)

    def draw_text(self, screen, font, color):
        img = font.render(self.text, True, color)
        screen.blit(img, (self.x, self.y))

    def is_clicked(self):
        mouseX,mouseY = pygame.mouse.get_pos()
        if mouseX >= self.x and mouseX <= self.x + self.width and mouseY >= self.y and mouseY <= self.y + self.height:
            print("Button works. ID: " + self.id)
            return self.id


