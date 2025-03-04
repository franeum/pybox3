import board
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer

PIXEL_PIN = board.NEOPIXEL
WIDTH = 5
HEIGHT = 5

PIXELS = neopixel.NeoPixel(
    PIXEL_PIN,
    WIDTH * HEIGHT,
    brightness=0.2,
    auto_write=False,
)

pixel_framebuf = PixelFramebuffer(
    PIXELS,
    WIDTH,
    HEIGHT,
    alternating=False
)