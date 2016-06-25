import pytest
import autocisco
import os
interface = "interfaceOutput.txt";
def test_ParseOnlyValidLines():
  lst = {}
  lst = autocisco.parse_int(interface)
  # file has 61 port 
  assert(len(lst)==61)

def test_ParseGetAllPorts():
  lst = {}
  lst = autocisco.parse_int(interface)
  assert('Gi1/1' in lst)
  assert('LongPortName' in lst)
  assert('Gi5/1' in lst)
  assert('LongPortNameWithLabel' in lst)


def test_readWholeFileIfExists():
  lst = {}
  lst = autocisco.readFile(interface)
  # file has 95 lines
  assert(len(lst)>56)

def test_returnErrorIfFileNotExists():
  lst = {}
  lst = autocisco.readFile("notExists.txt")
  # file has 95 lines
  assert(type(lst) == type(None)) 

def test_writeToFile():  
  autocisco.writeFile("test.txt","content of File")   
  assert(os.path.exists("test.txt") == True) 

def test_showHostList(capsys): 
  autocisco.printHostList(interface) 
  lines = autocisco.readFile(interface)
  output, err = capsys.readouterr()
  assert(len(output.split('\n')) > len(lines) )


def test_showInterfaceStatus(capsys): 
  autocisco.showInterfaceStatus(interface)   
  lines = autocisco.readFile(interface)  
  output, err = capsys.readouterr()
  assert(len(output.split('\n')) > len(lines) )