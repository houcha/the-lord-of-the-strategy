import os
import sys
import pygame
# project modules #
from game import Game
from game_objects import empire, races, map
from AI import AI
from interface.interface import Interface
from interface import click_handler
import configs
import user_configs
import image as img


def _clear_callback(surf, rect):
    surf.fill(map.Map().color, rect)


def finish_game(win: bool, screen: pygame.Surface):
    """ Called when game is finished. """

    if win:
        pygame.draw.rect(screen, pygame.Color('yellow'), screen.get_rect())
        final_message = 'You win!'
    else:
        pygame.draw.rect(screen, pygame.Color('red'), screen.get_rect())
        final_message = 'You lost...'
    font = pygame.font.SysFont(name='Ani', size=100)
    screen.blit(font.render(final_message, True, pygame.Color('black')),
                (screen.get_width() // 3 + 80, screen.get_height() // 5))
    screen.blit(font.render('To restart the game, press Space.', True, pygame.Color('black')),
                (screen.get_width() // 6, screen.get_height() // 4 + 150))
    screen.blit(font.render('To exit, press ESC.', True, pygame.Color('black')),
                (screen.get_width() // 4 + 30, screen.get_height() // 4 + 300))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                os.execl(sys.executable, sys.executable, *sys.argv)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return


def play_game():
    """ Function which starts the game. """

    # pygame initialization starts.
    pygame.init()
    screen = pygame.display.set_mode(configs.SCR_SIZE)
    pygame.display.set_caption("the Lord of the Strategy")
    icon_surf = img.get_image().ICON
    pygame.display.set_icon(icon_surf)
    clock = pygame.time.Clock()

    if not pygame.font.get_init():
        raise SystemExit("Fonts are out-of-service")
    # pygame initialization finishes.

    # Game objects initialization starts.
    player_empire = empire.Empire(user_configs.EMPIRE_RACE, name=user_configs.EMPIRE_NAME)
    enemy_empire = empire.Empire(races.DWARFS, name='Durden')

    game = Game(player_empire, enemy_empire)
    interface = Interface(player_empire, enemy_empire)

    player_empire.set_city(user_configs.CITY_NAME)
    player_default_city = player_empire.get_city(user_configs.CITY_NAME)
    player_default_city.rect.x = 500
    player_default_city.rect.centery = map.Map().rect.centery

    enemy_empire.set_city("Nuhen")
    enemy_default_city = enemy_empire.get_city("Nuhen")
    enemy_default_city.rect.right = map.Map().rect.right - 700
    enemy_default_city.rect.centery = map.Map().rect.centery
    AI(enemy_empire)
    # Game objects initialization finishes.

    # `rendered` is a group of objects has been drawn on map last loop iteration.
    rendered = None

    while True:
        mouse_pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True

        key = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pressed:
            click_handler.handle_click(mouse_pos)

        # AI is singleton, which has been initialized before.
        AI().play_step()

        # If any of empires is out of cities, the game is finished.
        if not player_empire.alive() or not enemy_empire.alive():
            finish_game(win=player_empire.alive(), screen=screen)
            return

        interface.move_view(key, mouse_pos)
        # Place objects on map.
        if rendered is not None:
            game.objects.clear(map.Map().image, _clear_callback)
        # Update objects.
        game.objects.update()
        # Update the group of last drawn objects.
        rendered = game.objects.draw(map.Map().image)
        interface.draw_interface(screen)

        # Show screen.
        pygame.display.flip()
        # Cap the framerate.
        clock.tick(50)


if __name__ == '__main__':
    play_game()
