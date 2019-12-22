import pytest

from keithley_daq6510.visa_instrument import VisaInstrument


@pytest.fixture
def device(resource_manager):
    dev = VisaInstrument(name='Generic VISA device',
                         address='GPIB::1::INSTR',
                         read_term='\n',
                         write_term='\n',
                         resource_manager=resource_manager)
    yield dev


def test_init():
    pass
