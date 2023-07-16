import pygame

class pycratsh:
    """
    Scratch + python = pycratch
    Make games with lots of joys!
    """
    def __init__(self,window_width,window_height,fps):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height
        self.WINDOW = pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.FPS = fps

    def init(self):
        """
        you have to write this toward begin!
        """
        import pygame
        pygame.init()
    
    def tick(self):
        self.CLOCK.tick(self.FPS)

    class Sprite(pygame.sprite.Sprite):
        """
        Creat a sprite!
        """
        def __init__(self,width,height,image_path,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(image_path)

            self.rect = self.image.get_rect()
            self.width = width
            self.height = height
            
            self.x = x
            self.y = y
        def resize(self, new_width, new_height):
            self.width = new_width
            self.height = new_height
            self.image = pygame.transform.scale(self.image, (new_width, new_height))
        def draw(self, surface):
            surface.blit(self.image, (self.x, self.y))
        

""" ---------------------------------------- """

pc = pycratsh(600,600,60)

pc.init()

class Dog(pc.Sprite):
    def move(self,speed):
        self.x += 5
        self.y += 1

window = pc.WINDOW
running = True

dog = Dog(200,200,"images\\cat1.svg",100,100)

while running:
    pc.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(pc.WHITE)

    pygame.display.flip()

pygame.quit()










