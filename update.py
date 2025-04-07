#!/usr/bin/env python3

from pathlib import Path
import shutil


def copia_cartella(src: Path, dst: Path, overwrite: bool = False):
    """
    Copia una cartella da src a dst in modo multipiattaforma.

    Args:
        src: Percorso sorgente (Path object)
        dst: Percorso destinazione (Path object)
        overwrite: Se True, sovrascrive la cartella esistente

    Solleva:
        FileNotFoundError: se src non esiste
        FileExistsError: se dst esiste e overwrite=False
    """
    if not src.exists():
        raise FileNotFoundError(f"La cartella sorgente {src} non esiste")

    if dst.exists():
        if overwrite:
            shutil.rmtree(dst)
        else:
            raise FileExistsError(f"La cartella destinazione {dst} esiste già")

    shutil.copytree(src, dst)
    print(f"Cartella copiata da '{src}' a '{dst}'")


# Esempio di utilizzo
if __name__ == "__main__":
    # Usa Path per creare percorsi compatibili con qualsiasi OS
    sorgente = Path("./mpy/pybox")
    destinazione = Path("/media/neum/CIRCUITPY/lib/pybox")

    try:
        copia_cartella(sorgente, destinazione, overwrite=True)
    except Exception as e:
        print(f"Errore: {e}")
