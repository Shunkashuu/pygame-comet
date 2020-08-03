import pygame
from player import Player
from monster import Monster
pygame.init()


# create a second class that will represent the game.
class Game:

    def __init__(self):
        # define if the game has started or not
        self.is_playing = False
        # generate the player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # group of monsters
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # reset the game, remove the monsters, reset the player to 100 of life
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # apply the player's image
        screen.blit(self.player.image, self.player.rect)

        # update the player life bar
        self.player.update_health_bar(screen)

        # retrieve the player's shots
        for projectile in self.player.all_projectile:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # apply all the images of the monsters group
        self.all_monsters.draw(screen)

        # apply all the images of the projectile group
        self.player.all_projectile.draw(screen)

        # check if the player wishes to go left or right
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    # mask is the hit-box principle
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)