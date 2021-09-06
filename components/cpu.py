from .common import to_bin
from enum import Enum
from .address import Address, ADDRESS_SIZE
from .cache import OperationResult

class OperationType(Enum):
  WRITE = "1"
  READ = "0"

def cpu_process(request:str, cache:dict, data_memory:list) -> str:
  instructions = request.split(" ")

  b_address = to_bin(instructions[0], ADDRESS_SIZE)
  addr = Address(b_address)

  operation = OperationType(instructions[1])
  
  data = ""
  if operation == OperationType.READ:
    return find_address_in_cache(addr, cache)
  elif operation == OperationType.WRITE:
    data = instructions[2]
    if cache[addr.index].valid:
      data_memory.append(cache[addr.index].data)
      cache[addr.index].data = data
      cache[addr.index].tag = addr.tag
    else:
      cache[addr.index].valid = 1
      cache[addr.index].tag = addr.tag
      cache[addr.index].data = data
    return OperationResult.WRITE

def search_address_in_memory(address:Address, memory:list) -> bool:
  for m in memory:
    if address.full_address == m:
      return True
  return False

def find_address_in_cache(address:Address, cache:dict) -> OperationResult:
  if cache[address.index].tag == address.tag:
    return OperationResult.HIT

  cache[address.index].tag = address.tag
  cache[address.index].valid = 1
  cache[address.index].data = address.full_address
  return OperationResult.MISS
