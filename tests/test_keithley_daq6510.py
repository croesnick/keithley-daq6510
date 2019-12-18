#!/usr/bin/env python

"""Tests for `keithley_daq6510` package."""

from keithley_daq6510.keithley_daq6510 import main


def test_noop():
    assert main() is None
