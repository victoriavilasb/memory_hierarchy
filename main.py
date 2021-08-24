from components.cache import empty_cache
from components.cpu import cpu_process
import sys

def main(filename):
  f = open(filename, "r")
  cpu_requests = f.readlines()

  cache = empty_cache()
  data_memory = list()

  op_results = {
    "W": 0,
    "M": 0,
    "H": 0
  }
  request_result = []

  for request in cpu_requests:
    result = cpu_process(request, cache, data_memory)
    op_results[result] += 1
    request_result.append("{} {}".format(request, result))

if __name__ == "__main__":
  main(sys.argv[1])