from typing import Optional

from pyvisa import ResourceManager


class VisaInstrument:
    def __init__(self, name: str, address: str, terminator: str, rm: Optional[ResourceManager] = None):
        self.name = name
        self.address = address
        self.terminator = terminator

        self.rm = rm if rm is not None else ResourceManager()
