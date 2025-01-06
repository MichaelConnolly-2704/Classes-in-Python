import pygame

pygame.init()

screen_width = 1000
screen_length = 1000

surface = pygame.display.set_mode((screen_width,screen_length))

bg = (55,50,250)
rectcol = (255,100,200)

class Rect1:
    def __init__(self,name,x,y,width,height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_UP]:
            self.y -=5
        if keys[pygame.K_DOWN]:
            self.y +=5

    def draw(self, surface):
    # Draw the rectangle on the surface (screen)
        pygame.draw.rect(surface, rectcol, (self.x, self.y, self.width, self.height))

rect = Rect1("Michael's Rect",100,100,150,100)   







# Main loop
run = True
while run:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Update rectangle's position based on key presses
    rect.Movement()

    # Fill background and draw rectangle
    surface.fill(bg)
    rect.draw(surface)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()



        