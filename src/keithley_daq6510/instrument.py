from typing import Optional

from pyvisa import ResourceManager

from .scpi.operation import Operation
from .visa_instrument import VisaInstrument


class Instrument(VisaInstrument):
    idn = Operation('*IDN?')

    def __init__(self, name: str, address: str, read_term: str = '\n', write_term: str = '\n',
                 resource_manager: Optional[ResourceManager] = None):
        super().__init__(name=name, address=address, read_term=read_term, write_term=write_term,
                         resource_manager=resource_manager)
