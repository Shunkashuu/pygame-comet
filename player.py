import pygame
from projectile import Projectile
pygame.init()

# to create a first class that will represent our player.
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5  # move speed
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()  # rectangle creation
        self.rect.x = 400
        # value from the top of the screen
        self.rect.y = 500

    def launch_projectile(self):
        # create a new instance of the projectile class
        self.all_projectile.add(Projectile(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity