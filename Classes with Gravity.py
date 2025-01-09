import pygame

# Initialize Pygame
pygame.init()

screen_width = 1000
screen_height = 800

# Fix the width/height order
screen = pygame.display.set_mode((screen_width, screen_height))

bg = (255, 200, 255)

class Player1:
    def __init__(self, image_path, x, y, colour):
        org_image = pygame.image.load('Hero.png')
        self.image = pygame.transform.scale(org_image,(50,50))  # Store directly as image instead of image_path
        self.x = x
        self.y = y 
        self.colour = colour
        self.speed = 0.3
        #Add new attributes for gravity
        self.velocity_y = 0.9
        self.gravity = 0.3      
        self.jump_speed = -8
        self.is_jumping = False
        #Horizontal movement 
    def move(self, keys):
        # Horizontal movement
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed    

        # Jumping 
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = self.jump_speed
            self.is_jumping = True

        # Apply gravity (fixed indentation - should run every frame)
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # Ground collision
        if self.y > screen_height - 50:  # 50 is player height
            self.y = screen_height - 50
            self.velocity_y = 0
            self.is_jumping = False
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))  # Now self.image exists

# Create hero object
hero = Player1("Hero.png", 500, 500, (10,10,10))

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Calling movement 
    keys = pygame.key.get_pressed()
    hero.move(keys)

    screen.fill(bg)
    hero.draw(screen)
    pygame.display.update()
    
pygame.quit()

