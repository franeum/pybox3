#!/usr/bin/env python3

import sys
import mpy_cross as mpy
from pathlib import Path
import shutil
import time

_input, output = Path(".") / Path(sys.argv[1]), Path(".") / Path(sys.argv[2])

print("GENERATING MPY...")
for file in _input.glob("*.py"):
    mpy.run(f"{file}")

time.sleep(1)
print("\t...done")

print("MOVE TO DESTINATION")

for file in _input.glob("*.mpy"):
    shutil.copy(file, output)
    Path(file).unlink()

print("\t...done")
