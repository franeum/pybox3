"""
*This module help you to manage fixed rectangle of RGB leds inside the matrix*

---

Examples:
    >>> from pybox.led import LED
    >>> from pybox.color import *
    >>> led = LED()
    >>> led.color = BLUE
    # turn on the led
    >>> led.on()
    # turn off the led
    >>> led.off()
"""

from pybox.matrix import MATRIX


class LED:
    """LED class.

    Args:
        target (str, optional): led to drive, 'internal', 'external' or a board string (i.e. board.GP18).
        color (tuple[int], optional): color in (r, g, b) format.
        brightness (float, optional): value between 0.0 and 1.0.

    Examples:
        >>> led = LED()
        >>> led.color = BLUE
        >>> led.on()
    """

    def __init__(self, color=None, brightness=0.25):
        self.led = MATRIX(color=color, brightness=brightness)
        self.toggler = 0

    def on(self, color=None):
        "Turn on the led"
        self.led.rect(1, 1, 3, 3, color=color)
        self.toggler = 1

    def off(self):
        "Turn off the led"
        self.led.off()
        self.toggler = 0

    def toggle(self):
        "Toggle led between on and off"
        if self.toggler == 1:
            self.off()
            self.toggler = 0
        else:
            self.on()

    def deinit(self):
        "Free the led to use the pin connected to it for another purpose"
        self.led.deinit()

    @property
    def color(self):
        """Get/Set color of the led

        Returns:
            color: color of the led in integer format
        """
        return self.led.color

    @color.setter
    def color(self, col):
        self.led.color = col

    @property
    def brightness(self) -> float:
        """Get/Set brightness of the matrix.

        Returns:
            brightness: brightness of the matrix in `float` format
        """
        return self.led.brightness

    @brightness.setter
    def brightness(self, value: float):
        self.led.brightness = value
