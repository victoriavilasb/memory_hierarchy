from common import to_bin
from enum import Enum
from address import Address, ADDRESS_SIZE

class OperationType(Enum):
  WRITE = 1
  READ = 0

def cpu_process(request:str, cache:dict, data_memory:list) -> str:
  instructions = request.split(" ")

  b_address = to_bin(instructions[0], ADDRESS_SIZE)
  addr = Address(b_address)

  operation = OperationType(instructions[1])
  
  data = ""
  if operation == OperationType.WRITE:
    data = instructions[2]

  raise ValueError("Missing implementation")
