# Sample Test passing with nose and pytest
# from lab_instruments.serial_instruments import SerialInstrument
from serial_instrument import SerialInstrument


def test_pass():
    assert True, "dummy sample test"


def test_class_serial_instrument_exist():
    instrument = SerialInstrument()
    assert isinstance(instrument, SerialInstrument)
