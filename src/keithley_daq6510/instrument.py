from typing import Optional

from pyvisa import ResourceManager

from .visa_instrument import VisaInstrument


class Instrument(VisaInstrument):
    def __init__(self, name: str, address: str, terminator: str = '\n', rm: Optional[ResourceManager] = None):
        super().__init__(name=name, address=address, terminator=terminator, rm=rm)
