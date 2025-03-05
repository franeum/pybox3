import board
import analogio
import time


POTS = [None, board.A0, board.A1]
TYPE_ERROR = "__init__() missing 1 required positional argument: 'pot_number'"
VALUE_ERROR = "argument 'pot_number' must be 1 or 2"
AVG_SIZE = 16


class POT:
    def __init__(self, pot_number=None):
        if pot_number is None:
            raise TypeError(TYPE_ERROR)
        if pot_number not in [1, 2]:
            raise ValueError(VALUE_ERROR)

        self._adc = analogio.AnalogIn(POTS[pot_number])
        self._array = [0] * AVG_SIZE
        self._counter = 0

    @property
    def midivalue(self):
        return 127 - (self._adc.value >> 9)

    @property
    def value(self):
        _value = max(500, self._adc.value)
        _value = min(65000, _value) - 500
        rounded = round(_value / 64500, 3)
        self._array[self._counter] = rounded
        self._counter += 1

        if (self._counter > (AVG_SIZE - 1)):
            self._counter = 0

        return round(sum(self._array) / AVG_SIZE, 3)

    @property
    def rawvalue(self):
        return (0XFFFF - self._adc.value) >> 4


if __name__ == '__main__':
    pot = POT()
    while True:
        print(f"{pot.value},\t{pot.midivalue}")
        time.sleep(0.1)
