import pytest
import autocisco


def test_ParseReadWholeFile():
  lst = {}
  lst = autocisco.parse_int("interfaceOutput.txt")
  # file has 10 lines
  assert(len(lst)==10)

def test_ParseGetAllPorts():
  lst = {}
  lst = autocisco.parse_int("interfaceOutput.txt")
  assert('Gi1/1' in lst)
  assert('LongPortName' in lst)
  assert('Gi5/1' in lst)
  assert('LongPortNameWithLabel' in lst)
