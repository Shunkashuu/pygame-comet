import pygame
from projectile import Projectile
pygame.init()


# to create a first class that will represent our player.
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
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

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_health_bar(self, surface):
        # draw the health bar
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def launch_projectile(self):
        # create a new instance of the projectile class
        self.all_projectile.add(Projectile(self))

    def move_right(self):
        # if the player is not colliding with a monster.
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity