import board
import simpleio

BUZZERS = [None, board.GP14, board.GP8]
TYPE_ERROR = "__init__() missing 1 required positional argument: 'buz_number'"
VALUE_ERROR = "argument 'buz_number' must be 1 or 2"


class TONE:
    def __init__(self, buz_number=None):
        if buz_number is None:
            raise TypeError(TYPE_ERROR)
        if buz_number not in [1, 2]:
            raise ValueError(VALUE_ERROR)

        self._pin = BUZZERS[buz_number]

    def play(self, note=440, duration=1):
        simpleio.tone(self._pin, note, duration)

    def mplay(self, midinote, duration=1):
        note = mtof(midinote)
        self.play(note, duration)


def mtof(m):
    return int(2**((m-69) / 12) * 440)
