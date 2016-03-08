#! /usr/bin/python

import getCredentials 

status = getCredentials.api.GetStreamSample()


# start random streamer for the timeline
# this script does not end, has to be stopped manually.
for line in status:
  try:
    print line
    print '--'*10
  except KeyError, httplib.IncompleteRead:
    continue

