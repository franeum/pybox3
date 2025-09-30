from adafruit_pixel_framebuf import PixelFramebuffer
from neopixel import NeoPixel
from pybox.color import RED, OFF
import board

PIXEL_PIN = board.NEOPIXEL
WIDTH = 5
HEIGHT = 5


def _colortuple2colorint(color):
    r, g, b = color
    return (r << 16) + (g << 8) + b


def _colorint2colortuple(color):
    return (color >> 16) & 255, (color >> 8) & 255, color & 255


def _check_color_format(color):
    if isinstance(color, tuple):
        return _colortuple2colorint(color)
    else:
        return color


def _index2xy(index, n_rows, n_cols):
    return index % n_rows, index // n_cols


def _chek_n_of_args(args, list_of_numbers):
    if len(args) not in list_of_numbers:
        raise TypeError("Wrong number of arguments")


class PIXEL:
    def __init__(self, buffer, index, color):
        self.buffer = buffer
        self.index = index
        self._color = color

    def on(self):
        x, y = _index2xy(self.index, WIDTH, HEIGHT)
        self.buffer.pixel(x, y, color=self._color)
        self.buffer.display()

    def off(self):
        x, y = _index2xy(self.index, WIDTH, HEIGHT)
        self.buffer.pixel(x, y, color=0x000000)
        self.buffer.display()

    def toggle(self):
        x, y = _index2xy(self.index, WIDTH, HEIGHT)
        current_color = self.buffer.pixel(x, y)  # ottieni il colore attuale (int)

        if current_color != 0x000000:
            self.off()
        else:
            self.on()

    @property
    def color(self):
        return _colorint2colortuple(self._color)

    @color.setter
    def color(self, col=RED):
        self._color = _check_color_format(col)


class MATRIX:
    def __init__(self, color=RED, brightness=0.25):
        self._pixels = NeoPixel(
            PIXEL_PIN, WIDTH * HEIGHT, brightness=brightness, auto_write=False
        )
        self.frame_buf = PixelFramebuffer(
            self._pixels, WIDTH, HEIGHT, alternating=False
        )

        self._global_col = _check_color_format(color)
        self._col = [self._global_col] * (WIDTH * HEIGHT)
        self.is_on = False

        self._singletons = [
            PIXEL(self.frame_buf, x, self._global_col) for x in range(WIDTH * HEIGHT)
        ]

    def fill(self, color):
        """Fill the matrix with a color"""
        col = _check_color_format(color)
        self.frame_buf.fill(col)
        self.frame_buf.display()

        self.is_on = color > 0

        return None

    def fill_rect(self, *args, **kwargs):
        """Draw a fill rect"""
        _chek_n_of_args(args, [3, 4])

        if len(args) == 3:
            index, width, height = args
            x, y = _index2xy(index, WIDTH, HEIGHT)
        else:
            x, y, width, height = args

        _color = kwargs.get("color")
        _color = _check_color_format(_color) if _color is not None else self._global_col

        self.is_on = _color > 0

        self.frame_buf.fill_rect(x, y, width, height, _color)
        self.frame_buf.display()

    def rect(self, *args, **kwargs):
        """Draw a (empty) rect"""
        _chek_n_of_args(args, [3, 4])

        if len(args) == 3:
            index, width, height = args
            x, y = _index2xy(index, WIDTH, HEIGHT)
        else:
            x, y, width, height = args

        _color = kwargs.get("color")
        _color = _check_color_format(_color) if _color is not None else self._global_col

        self.is_on = _color > 0

        self.frame_buf.rect(x, y, width, height, _color)
        self.frame_buf.display()

    def line(self, *args, **kwargs):
        """Draw a line from a point to another"""
        _chek_n_of_args(args, [2, 4])

        if len(args) == 2:
            start, end = args
            x_0, y_0 = _index2xy(start, WIDTH, HEIGHT)
            x_1, y_1 = _index2xy(end, WIDTH, HEIGHT)
        else:
            x_0, y_0, x_1, y_1 = args

        _color = kwargs.get("color")
        _color = _check_color_format(_color) if _color is not None else self._global_col

        self.is_on = _color > 0

        self.frame_buf.line(x_0, y_0, x_1, y_1, _color)
        self.frame_buf.display()

    def off(self):
        "Off the whole matrix"
        self.frame_buf.fill(0x000000)
        self.frame_buf.display()
        self.is_on = 0

    def on(self, color=None):
        "On the whole matrix"
        if color is not None:
            self._global_col = _check_color_format(color)

        self.frame_buf.fill(self._global_col)
        self.frame_buf.display()
        self.is_on = 1

    def toggle(self):
        "Toggle between on and off"
        if self.is_on == 1:
            self.off()
            self.is_on = 0
        else:
            self.on()
            self.is_on = 1

    def pixel(self, *args, **kwargs):
        "Set a single pixel"
        _chek_n_of_args(args, [1, 2])

        if len(args) == 1:
            index = args[0]
            x, y = _index2xy(index, WIDTH, HEIGHT)
        else:
            x, y = args

        _color = kwargs.get("color")
        _color = _check_color_format(_color) if _color is not None else self._global_col

        self.frame_buf.pixel(x, y, color=_color)
        self.frame_buf.display()

    def deinit(self):
        "Free the pin of the matrix"
        self._pixels.deinit()

    @property
    def color(self):
        """Get/Set color of the matrix.

        Returns:
            color: color of the matrix in triple (r,g,b) format
        """
        return _colorint2colortuple(self._global_col)

    @color.setter
    def color(self, col=RED):
        self._global_col = _check_color_format(col)

    @property
    def brightness(self) -> float:
        """Get/Set brightness of the matrix.

        Returns:
            brightness: brightness of the matrix in `float` format
        """
        return self._pixels.brightness

    @brightness.setter
    def brightness(self, value: float):
        self._pixels.brightness = value

    def __setitem__(self, index: int, color: tuple[int]) -> None:
        x, y = _index2xy(index, WIDTH, HEIGHT)
        self.frame_buf.pixel(x, y, color=_check_color_format(color))
        self.frame_buf.display()

    def __getitem__(self, index: int) -> PIXEL:
        if not 0 <= index < WIDTH * HEIGHT:
            raise IndexError("Pixel index out of range.")

        return self._singletons[index]
