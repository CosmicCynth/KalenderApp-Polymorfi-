class Button:
    def __init__(self, x, y, width, height, text, scene):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.scene = scene

        self.colors = (255, 255, 255)
        self.textColor = (0,0,0)

    def draw_text(self, screen, font, color):
        img = font.render(self.text, True, color)
        screen.blit(img, (self.x, self.y))

    def is_clicked(self):
        return "labubu"

