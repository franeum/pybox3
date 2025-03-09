import random

RED = 0xff0000  # (255, 0, 0)
GREEN = 0x00ff00  # (0, 255, 0)
BLUE = 0x0000ff  # (0, 0, 255)
YELLOW = 0xff9600  # (255, 150, 0)
CYAN = 0x00ffff  # (0, 255, 255)
PURPLE = 0xb400ff  # (180, 0, 255)
WHITE = 0xffffff  # (255, 255, 255)
PINK = 0xd20a64  # (210, 10, 100)
OFF = 0x000000  # (0, 0, 0)

__colors = [RED, GREEN, BLUE, YELLOW, CYAN, PURPLE, WHITE]


def get_random_color():
    return random.choice(__colors)
