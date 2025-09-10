#!/usr/bin/env python3

import sys
from pathlib import Path
import shutil
import time
import subprocess as sp

_input, _output = Path(".") / Path(sys.argv[1]), Path(".") / Path(sys.argv[2])

print("GENERATING MPY...")
for file in _input.glob("*.py"):
    sp.run(["./mpy-cross-linux-amd64-9.1.4.static", f"{file}"])

time.sleep(1)
print("\t...done")

print("MOVE TO DESTINATION")

for file in _input.glob("*.mpy"):
    shutil.copy(file, _output)
    Path(file).unlink()

print("\t...done")
