import pygame
pygame.init()

# to create a first class that will represent our player.
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5  # move speed
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()  # rectangle creation
        self.rect.x = 400
        # value from the top of the screen
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity