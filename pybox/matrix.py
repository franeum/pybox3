from adafruit_pixel_framebuf import PixelFramebuffer
from neopixel import NeoPixel
from pybox.color import RED, OFF
import board

PIXEL_PIN = board.NEOPIXEL
WIDTH = 5
HEIGHT = 5


def colortuple2colorint(color):
    r, g, b = color
    return (r << 16) + (g << 8) + b


def check_color_format(color):
    if isinstance(color, tuple):
        return colortuple2colorint(color)
    else:
        return color


def index2xy(index, n_rows, n_cols):
    return index % n_rows, index // n_cols


class PIXEL:
    def __init__(self, index):
        self.index = index


class MATRIX:
    def __init__(self, color=RED, brightness=0.25):
        self._pixels = NeoPixel(
            PIXEL_PIN,
            WIDTH * HEIGHT,
            brightness=brightness,
            auto_write=False
        )
        self.frame_buf = PixelFramebuffer(
            self._pixels,
            WIDTH,
            HEIGHT,
            alternating=False
        )

        self._global_col = check_color_format(color)
        self._col = [self._global_col] * (WIDTH * HEIGHT)
        self.total_toggler = False

    def fill(self, color):
        col = check_color_format(color)
        self.frame_buf.fill(col)
        self.frame_buf.display()

        self.total_toggler = color > 0

        return None

    def fill_rect(self, *args, **kwargs):
        if len(args) == 3:
            index, width, height = args
            x, y = index2xy(index, WIDTH, HEIGHT)
        elif len(args) == 4:
            x, y, width, height = args

        _color = kwargs.get('color')
        _color = check_color_format(
            _color) if _color is not None else self._global_col

        self.total_toggler = _color > 0

        self.frame_buf.fill_rect(x, y, width, height, _color)
        self.frame_buf.display()

    def rect(self, *args, **kwargs):
        if len(args) == 3:
            index, width, height = args
            x, y = index2xy(index, WIDTH, HEIGHT)
        elif len(args) == 4:
            x, y, width, height = args

        _color = kwargs.get('color')
        _color = check_color_format(
            _color) if _color is not None else self._global_col

        self.total_toggler = _color > 0

        self.frame_buf.rect(x, y, width, height, _color)
        self.frame_buf.display()

    # line(x_0, y_0, x_1, y_1, color)
    def line(self, *args, **kwargs):
        if len(args) == 2:
            start, end = args
            x_0, y_0 = index2xy(start, WIDTH, HEIGHT)
            x_1, y_1 = index2xy(end, WIDTH, HEIGHT)
        elif len(args) == 4:
            x_0, y_0, x_1, y_1 = args

        _color = kwargs.get('color')
        _color = check_color_format(
            _color) if _color is not None else self._global_col

        self.total_toggler = _color > 0

        self.frame_buf.line(x_0, y_0, x_1, y_1, _color)
        self.frame_buf.display()

    def off(self):
        self.frame_buf.fill(0x000000)
        self.frame_buf.display()
        self.total_toggler = 0

    def on(self, color=None):
        if color is not None:
            self._global_col = check_color_format(color)

        self.frame_buf.fill(self._global_col)
        self.frame_buf.display()
        self.total_toggler = 1

    def toggle(self):
        if self.total_toggler == 1:
            self.off()
            self.total_toggler = 0
        else:
            self.on()
            self.total_toggler = 1

    def pixel(self, *args, **kwargs):
        if len(args) == 1:
            index = args[0]
            x, y = index2xy(index, WIDTH, HEIGHT)
        elif len(args) == 2:
            x, y = args

        _color = kwargs.get('color')
        _color = check_color_format(
            _color) if _color is not None else self._global_col

        self.frame_buf.pixel(x, y, color=_color)
        self.frame_buf.display()

    def deinit(self):
        self._pixels.deinit()

    @property
    def color(self):
        return self._global_col

    @color.setter
    def color(self, col=RED):
        self._global_col = check_color_format(col)

    @property
    def brightness(self) -> float:
        """Get/Set color of the matrix.

        Returns:
            brightness: brightness of the matrix in `float` format
        """
        return self._pixels.brightness

    @brightness.setter
    def brightness(self, value: float):
        self._pixels.brightness = value
