#!/usr/bin/env python3

import sys
import mpy_cross as mpy
from pathlib import Path
import shutil

input, output = Path(".") / Path(sys.argv[1]), Path(".") / Path(sys.argv[2])
input_files = input.glob("*.py")


for file in input_files:
    mpy.run(f"{file}")
    shutil.copyfile(file, f"./{output}/{file.stem}.mpy")

for file in input.glob("*.mpy"):
    Path(file).unlink()
