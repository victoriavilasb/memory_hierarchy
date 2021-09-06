from components.cache import empty_cache
from components.cpu import cpu_process
from components.cache import OperationResult
import sys

def main(filename):
  f = open(filename, "r")
  cpu_requests = f.readlines()

  cache = empty_cache()
  data_memory = list()

  op_results = {
    OperationResult.WRITE: 0,
    OperationResult.MISS: 0,
    OperationResult.HIT: 0
  }

  request_result = []
  for request in cpu_requests:
    request = request.rstrip()
    result = cpu_process(request, cache, data_memory)
    op_results[result] += 1
    request_result.append("{} {}".format(request, result.value))

  reads = op_results[OperationResult.MISS] + op_results[OperationResult.HIT]
  print("READS: {}".format(reads))
  print("WRITES: {}".format(op_results[OperationResult.WRITE]))
  print("HITS: {}".format(op_results[OperationResult.HIT]))
  print("MISSES: {}".format(op_results[OperationResult.MISS]))
  print("HIT RATE: {0:.3}".format(op_results[OperationResult.HIT]/reads))
  print("MISS RATE: {0:.3}\n".format(op_results[OperationResult.MISS]/reads))

  for r in request_result:
    print(r)
    
if __name__ == "__main__":
  main(sys.argv[1])