# Sua cache tem a capacidade de armazenar 64 blocos. Cada bloco da cache contém 16 bytes, que
# correspondem a 4 palavras de 32 bits, que resultam em 128 bits no total.
TAG_SIZE = 2 
INDEX_SIZE = 6
OFFSET_SIZE = 5
ADDRESS_SIZE = 13

class Address:
  def __init__(self, address):
    self.offset = address[0:TAG_SIZE]
    self.index = address[TAG_SIZE:INDEX_SIZE+TAG_SIZE]
    self.tag = address[INDEX_SIZE+TAG_SIZE:ADDRESS_SIZE]