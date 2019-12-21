from typing import Optional

from pyvisa import ResourceManager
from pyvisa.resources import MessageBasedResource


class VisaInstrument:
    def __init__(self, name: str, address: str, terminator: str, rm: Optional[ResourceManager] = None):
        self.name = name
        self.address = address
        self.terminator = terminator

        self.rm = rm if rm is not None else ResourceManager()

        self.conn: MessageBasedResource = self.rm.open_resource(resource_name=self.name)

    @property
    def idn(self) -> str:
        return self.conn.query('*IDN?')
