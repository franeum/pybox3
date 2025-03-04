from pybox.matrix import MATRIX


class LED:
    def __init__(self):
        self.led = MATRIX()
        self.toggler = 0

    def on(self, color):
        self.led.rect(1, 1, 3, 3, color=color)
        self.toggler = 1

    def off(self):
        self.led.off()
        self.toggler = 0

    def toggle(self):
        if self.toggler == 1:
            self.off()
            self.toggler = 0
        else:
            self.on()

    def deinit(self):
        self.led.deinit()

    @property
    def color(self):
        return self.led.color

    @color.setter
    def color(self, col):
        self.led.color = col

    @property
    def brightness(self) -> float:
        """Get/Set color of the matrix.

        Returns:
            brightness: brightness of the matrix in `float` format
        """
        return self.led.brightness

    @brightness.setter
    def brightness(self, value: float):
        self.led.brightness = value
