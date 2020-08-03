import pygame
pygame.init()


# define the class that will handle the player's projectile
class Projectile(pygame.sprite.Sprite):

    # define the constructor of this class
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # spin the bullet
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # check to see if the projectile collides with a monster.
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            # remove the bullet
            self.remove()

        # check if the projectile is no longer present on the screen
        if self.rect.x > 1080:
            # remove the projectile from the screen
            self.remove()