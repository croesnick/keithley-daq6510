import pytest
from keithley_daq6510.instrument import Instrument

@pytest.fixture
def device(resource_manager):
    dev = Instrument(name='DAQ Test', address='IPX', rm=resource_manager)


def test_init():
    pass
