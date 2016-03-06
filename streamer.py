import twitter
import httplib


status = api.GetStreamSample()

for line in status:
  try:
    print line
    print '--'*10
  except KeyError, httplib.IncompleteRead:
    continue
