import pytest
import autocisco


def test_ParseReadWholeFile():
  lst = autocisco.parse_int("interfaceOutput.txt")
  # file has 10 lines and header
  assert(len(lst)==11)

def test_ParseGetAllPorts():
  lst = autocisco.parse_int("interfaceOutput.txt")
  assert('Gi1/1' in lst)
  assert('LongPortName' in lst)
  assert('Gi5/1' in lst)
  assert('LongPortNameWithLabel' in lst)
