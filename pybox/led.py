from pybox.matrix import MATRIX
from pybox.color import *

def LED(color: tuple[int] = RED, brightness: float = 0.25):
    matrix = MATRIX(color, brightness)
    return matrix[12]