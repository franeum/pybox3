#!/usr/bin/env python3

from pathlib import Path
import shutil
import subprocess as sp
import sys

# Configurazione
MPY_CROSS = Path("./mpy-cross-linux-amd64-9.1.4.static")  # compilatore
INPUT_DIR = Path("./src/pybox")
OUTPUT_DIR = Path("./mpy/pybox")


def main():
    if not MPY_CROSS.exists():
        print(f"❌ Errore: compilatore '{MPY_CROSS}' non trovato.")
        sys.exit(1)

    if not INPUT_DIR.exists():
        print(f"❌ Errore: la cartella sorgente '{INPUT_DIR}' non esiste.")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("🚀 Generazione dei file .mpy...")
    py_files = list(INPUT_DIR.glob("*.py"))
    if not py_files:
        print("⚠️ Nessun file .py trovato.")
        return

    for py_file in py_files:
        result = result = sp.run(
            [str(MPY_CROSS.resolve()), str(py_file)], capture_output=True, text=True
        )

        if result.returncode != 0:
            print(f"❌ Errore compilando {py_file.name}:\n{result.stderr.strip()}")
        else:
            print(f"✓ {py_file.name} compilato.")

    print("📦 Spostamento dei .mpy nella destinazione...")
    mpy_files = list(INPUT_DIR.glob("*.mpy"))
    for mpy_file in mpy_files:
        destination = OUTPUT_DIR / mpy_file.name
        shutil.copy(mpy_file, destination)
        mpy_file.unlink()
        print(f"→ {mpy_file.name} spostato in {OUTPUT_DIR}")

    print("✅ Tutto fatto!")


if __name__ == "__main__":
    main()
