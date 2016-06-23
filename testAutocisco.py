import pytest
import autocisco


def test_ParseInterfaceFile():
  lst = autocisco.parse_int("interfaceOutput.txt")
  # file has 10 lines and header
  assert(len(lst)==11)

