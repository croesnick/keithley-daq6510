"""Top-level package for Keithley DAQ6510 instrument sample library."""

__author__ = """Carsten Rösnick-Neugebauer"""
__email__ = 'croesnick@gmail.com'
__version__ = '0.0.1'

import logging

logging.getLogger('keithley_daq6510').addHandler(logging.NullHandler())
