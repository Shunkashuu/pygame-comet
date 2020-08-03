import pygame
import math
from game import Game
pygame.init()


# generate the game window
pygame.display.set_caption("Pygame Comet")
screen = pygame.display.set_mode((1080, 720))

# import the game background
background = pygame.image.load('assets/bg.jpg')

# import, loading banner
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# import, loading the launch button
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeu
game = Game()

# to prevent the window from closing, says that the game is running
running = True

# loop as long as this condition is true will repeat itself as long as the game is active.
while running:

    # apply the background of the game
    screen.blit(background, (0, -200))

    # check if the game has started or not
    if game.is_playing:
        # trigger the instructions of the
        game.update(screen)
    # check if the game hasn't started yet
    else:
        # add welcome screen
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the mouse collides with the play button
            if play_button_rect.collidepoint(event.pos):
                # put the game on run mode
                game.start()