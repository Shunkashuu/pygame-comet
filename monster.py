import pygame
import random
pygame.init()


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        # inflict damage
        self.health -= amount

        # check if his new hit points are less than or equal to 0
        if self.health <= 0:
            # reappear as a new monster
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        # draw the health bar
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # the move is made only if there is no collision with a group of players
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # if the monster collides with the player
        else:
            # do damage
            self.game.player.damage(self.attack)