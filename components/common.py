def to_bin(decimal:str, size:int) -> str:
  return bin(int(decimal)).replace('0b', '').zfill(size)