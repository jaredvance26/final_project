import os
import arcade

MAX_X = 800
MAX_Y = 600
SCREEN_TITLE = 'Pac-Man'

ACTOR_SCALE = .25
MOVE_SCALE = 7

BLINKY_X = MAX_X/2
CLYEDE_X = MAX_X/2 - 50
INKY_X = MAX_X/2 + 50
PINKY_X = MAX_X/2 + 100

BLINKY_Y = MAX_Y/2
CLYEDE_Y = MAX_Y/2
INKY_Y = MAX_Y/2
PINKY_Y = MAX_Y/2


PATH = os.path.dirname(os.path.abspath(__file__))
PACMAN_IMAGE = os.path.join(PATH, '..', 'pac-assets', 'character-pac-man.png')
BLINKY_IMAGE = os.path.join(PATH, '..', 'pac-assets', 'character-blinky.png')
CLYDE_IMAGE = os.path.join(PATH, '..', 'pac-assets', 'character-clyde.png')
INKY_IMAGE = os.path.join(PATH, '..', 'pac-assets', 'character-inky.png')
PINKY_IMAGE = os.path.join(PATH, '..', 'pac-assets', 'character-pinky.png')
MOVE_SOUND = arcade.load_sound(os.path.join(PATH, '..', 'pac-assets', 'pacman_chomp.wav'))