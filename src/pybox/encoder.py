#!/usr/bin/env python3

"""Module to manage rotary encoder"""

import rotaryio
import board


class SuperEnc:
    """Superclass SuperEnc. You shouldn't use this directly."""

    def __init__(self):
        self.enc = rotaryio.IncrementalEncoder(board.GP3, board.GP2)


class ENC(SuperEnc):
    """This class manages the rotary encoder returning 1 or -1,
    depending on direction of the rotation
    """

    def __init__(self, _min=0, _max=127, _start=None):
        super().__init__()
        self.position = self.enc.position
        self.last_position = self.enc.position
        self._min = _min
        self._max = _max

        if _start is None:
            self._value = _min
        else:
            self._value = _start

    def __force_bounds(self, value):
        current = min(self._max, value)
        current = max(current, self._min)
        return current

    def update(self):
        """Update encoder position. To be called every time you need new value"""
        self.last_position = self.position
        self.position = self.enc.position
        self._value = self.__force_bounds(self._value + self.direction)

    @property
    def changed(self):
        """Verifies if the encoder value is changed.

        :return: True if the new position is different from the last, otherwise False
        """
        return self.position != self.last_position

    @property
    def direction(self):
        """Get direction. 1 if clockwise, -1 if counter-clockwise, 0 if no movement."""
        if self.position > self.last_position:
            return 1
        elif self.position < self.last_position:
            return -1
        return 0

    @property
    def minval(self):
        """Get/set min value"""
        return self._min

    @minval.setter
    def minval(self, value):
        self._min = value

    @property
    def maxval(self):
        """Get/set max value"""
        return self._max

    @maxval.setter
    def maxval(self, value):
        self._max = value

    @property
    def bounds(self):
        """Get/set (min, max) values"""
        return self._min, self._max

    @bounds.setter
    def bounds(self, _bounds):
        self._min, self._max = sorted(_bounds)

    @property
    def value(self):
        """Get/set value"""
        return self._value

    @value.setter
    def value(self, val):
        self._value = self.__force_bounds(val)
