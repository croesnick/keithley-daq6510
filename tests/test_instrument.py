import pytest

from keithley_daq6510.instrument import Instrument


@pytest.fixture
def device(resource_manager):
    dev = Instrument(name='Generic VISA device', address='GPIB::1::INSTR', resource_manager=resource_manager)
    yield dev


def test_init():
    pass


def test_idn(device):
    assert device.idn == 'Keithley Instruments Inc., Model DAQ 6510'
