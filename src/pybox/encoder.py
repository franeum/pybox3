#!/usr/bin/env python3

"""Module to manage rotary encoder"""

import rotaryio
import board


class SuperEnc:
    def __init__(self):
        self.enc = rotaryio.IncrementalEncoder(board.GP2, board.GP4)


class ENC(SuperEnc):
    def __init__(self):
        super().__init__()
        self.last_position = None

    def position(self):
        pass


class ENCMINMAX(ENC):
    def __init__(self, minval=0, maxval=127):
        self._min = minval
        self._max = maxval
        super().__init__()
