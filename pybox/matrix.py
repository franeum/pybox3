from adafruit_pixel_framebuf import PixelFramebuffer
from neopixel import NeoPixel
from pybox.color import RED, OFF
import board

PIXEL_PIN = board.NEOPIXEL
WIDTH = 5
HEIGHT = 5


def __colortuple2colorint(color):
    r, g, b = color
    return (r << 16) + (g << 8) + b


def __check_color_format(color):
    if isinstance(color, tuple):
        return __colortuple2colorint(color)
    else:
        return color


def __index2xy(index, n_rows, n_cols):
    return index % n_rows, index // n_cols


def __chek_n_of_args(args, list_of_numbers):
    if len(args) not in list_of_numbers:
        raise TypeError("Wrong number of arguments")


class PIXEL:
    def __init__(self, buffer, index, color):
        self.buffer = buffer
        self.index = index
        self._color = color

    def on(self):
        x, y = __index2xy(self.index, WIDTH, HEIGHT)
        self.buffer.pixel(x, y, color=self._color)
        self.buffer.display()

    def off(self):
        x, y = __index2xy(self.index, WIDTH, HEIGHT)
        self.buffer.pixel(x, y, color=0x000000)
        self.buffer.display()

    def toggle(self):
        if sum(self.buffer.buf[self.index:self.index+3]) != 0:
            self.off()
        else:
            self.on()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, col=RED):
        self._color = __check_color_format(col)


class MATRIX:
    def __init__(self, color=RED, brightness=0.25):
        self._pixels = NeoPixel(
            PIXEL_PIN, WIDTH * HEIGHT, brightness=brightness, auto_write=False
        )
        self.frame_buf = PixelFramebuffer(
            self._pixels, WIDTH, HEIGHT, alternating=False
        )

        self._global_col = __check_color_format(color)
        self._col = [self._global_col] * (WIDTH * HEIGHT)
        self.total_toggler = False

        self.singletons = [PIXEL(self.frame_buf, x, self._global_col)
                           for x in range(WIDTH * HEIGHT)]

    def fill(self, color):
        col = __check_color_format(color)
        self.frame_buf.fill(col)
        self.frame_buf.display()

        self.total_toggler = color > 0

        return None

    def fill_rect(self, *args, **kwargs):
        __chek_n_of_args(args, [3, 4])

        if len(args) == 3:
            index, width, height = args
            x, y = __index2xy(index, WIDTH, HEIGHT)
        else:
            x, y, width, height = args

        _color = kwargs.get("color")
        _color = (
            __check_color_format(
                _color) if _color is not None else self._global_col
        )

        self.total_toggler = _color > 0

        self.frame_buf.fill_rect(x, y, width, height, _color)
        self.frame_buf.display()

    def rect(self, *args, **kwargs):
        __chek_n_of_args(args, [3, 4])

        if len(args) == 3:
            index, width, height = args
            x, y = __index2xy(index, WIDTH, HEIGHT)
        else:
            x, y, width, height = args

        _color = kwargs.get("color")
        _color = (
            __check_color_format(
                _color) if _color is not None else self._global_col
        )

        self.total_toggler = _color > 0

        self.frame_buf.rect(x, y, width, height, _color)
        self.frame_buf.display()

    def line(self, *args, **kwargs):
        __chek_n_of_args(args, [2, 4])

        if len(args) == 2:
            start, end = args
            x_0, y_0 = __index2xy(start, WIDTH, HEIGHT)
            x_1, y_1 = __index2xy(end, WIDTH, HEIGHT)
        else:
            x_0, y_0, x_1, y_1 = args

        _color = kwargs.get("color")
        _color = (
            __check_color_format(
                _color) if _color is not None else self._global_col
        )

        self.total_toggler = _color > 0

        self.frame_buf.line(x_0, y_0, x_1, y_1, _color)
        self.frame_buf.display()

    def off(self):
        self.frame_buf.fill(0x000000)
        self.frame_buf.display()
        self.total_toggler = 0

    def on(self, color=None):
        if color is not None:
            self._global_col = __check_color_format(color)

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
        __chek_n_of_args(args, [1, 2])

        if len(args) == 1:
            index = args[0]
            x, y = __index2xy(index, WIDTH, HEIGHT)
        else:
            x, y = args

        _color = kwargs.get("color")
        _color = (
            __check_color_format(
                _color) if _color is not None else self._global_col
        )

        self.frame_buf.pixel(x, y, color=_color)
        self.frame_buf.display()

    def deinit(self):
        self._pixels.deinit()

    @property
    def color(self):
        return self._global_col

    @color.setter
    def color(self, col=RED):
        self._global_col = __check_color_format(col)

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

    def __setitem__(self, index: int, item: tuple[int]) -> None:
        # self._pixels[index] = self.__parse_color(index, item)
        pass

    def __getitem__(self, index: int) -> tuple[int]:
        # return PIXEL(self.frame_buf, index, self._global_col)
        return self.singletons[index]
