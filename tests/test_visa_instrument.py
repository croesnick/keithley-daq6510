def test_init():
    pass


def test_idn(device):
    assert device.idn == 'Keithley Instruments Inc., Model DAQ 6510'
