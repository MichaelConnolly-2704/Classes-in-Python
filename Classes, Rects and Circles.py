import pygame

screen_size = 1000

screen = pygame.display.set_mode((screen_size,screen_size))
bg = (250,250,250)


class Moving_Rectangle:
    def __init__(self,x,y,height, width,colour): #speed is not put in the arguments because it is going to be a set value within the Class
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colour = colour
        self.speed = 0.02

    
    def move(self, keys):
    # Move the player based on key inputs
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self,screen):
        pygame.draw.rect(screen,self.colour,(self.x,self.y,self.width,self.height))




class Moving_circle:
    def __init__(self,x,y,colour,rad):
        self.x = x
        self.y = y
        self.colour = colour
        self.rad = rad
        self.speed = 1


    def move(self,keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed       
        if keys[pygame.K_RIGHT]:
            self.x += self.speed    
        if keys[pygame.K_LEFT]:
            self.x -= self.speed

    def draw(self,screen):
        pygame.draw.circle(screen,self.colour,(self.x,self.y),self.rad)


My_rect = Moving_Rectangle(50,50,50,50, (255,0,100))
My_Circle = Moving_circle(50,100,(124,156,232),10)



#Main Game Loop

#Event handling 
run = True
while run:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            run = False


    #Back_Ground colour
    screen.fill(bg)

    #Inputs
    keys = pygame.key.get_pressed()
    My_Circle.move(keys)
    My_rect.move(keys)

    #Call to screen
    My_rect.draw(screen)
    My_Circle.draw(screen)

    pygame.display.update()





pygame.quit()


