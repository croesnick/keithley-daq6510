from typing import Optional

from pyvisa import ResourceManager
from pyvisa.resources import MessageBasedResource


class VisaInstrument:
    def __init__(self, name: str, address: str, read_term: str, write_term: str,
                 resource_manager: Optional[ResourceManager] = None):
        self.name = name
        self.address = address
        self.read_termination = read_term
        self.write_termination = write_term

        self.resource_manager = resource_manager if resource_manager is not None else ResourceManager()

        self.conn: MessageBasedResource = \
            self.resource_manager.open_resource(self.address,
                                                read_termination=self.read_termination,
                                                write_termination=self.write_termination)

    @property
    def idn(self) -> str:
        return self.conn.query('*IDN?')
