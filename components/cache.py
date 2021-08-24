from common import to_bin
from address import INDEX_SIZE

CACHE_SIZE = 64

class CacheRow:
  def __init__(self) -> None:
    self.valid = 0
    self.tag = ""
    self.data = ""

def empty_cache() -> dict:
  cache = {}

  for i in range(0, CACHE_SIZE):
    cache[to_bin(str(i), INDEX_SIZE)] = CacheRow()

  return cache

