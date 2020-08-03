import pygame
from game import Game
pygame.init()


# generate the game window
pygame.display.set_caption("Pygame Comet")
screen = pygame.display.set_mode((1080, 720))

# import the game background
background = pygame.image.load('assets/bg.jpg')

# charger le jeu
game = Game()

# to prevent the window from closing, says that the game is running
running = True

# loop as long as this condition is true will repeat itself as long as the game is active.
while running:

    # apply the background of the game
    screen.blit(background, (0, -200))

    # apply the player's image
    screen.blit(game.player.image, game.player.rect)

    # update the player life bar
    game.player.update_health_bar(screen)

    # retrieve the player's shots
    for projectile in game.player.all_projectile:
        projectile.move()

    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # apply all the images of the monsters group
    game.all_monsters.draw(screen)

    # apply all the images of the projectile group
    game.player.all_projectile.draw(screen)

    # check if the player wishes to go left or right
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # update screen
    pygame.display.flip()

    # if the player closes this window
    for event in pygame.event.get():
        # that the event is window-closing.
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detect if a player drops a key on the keyboard
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detect if the space key is pressed to launch the projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
