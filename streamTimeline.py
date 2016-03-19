#! /usr/bin/python

import getCredentials 

status = getCredentials.api.GetStreamSample()


# start random streamer for the timeline
# this script does not end, has to be stopped manually.
# line is the entry for each tweet
# it is a python dictionary, for all the keys, check README file.

count = 0
maxChars = 0
for line in status:
  try:
    if line.has_key('text') and line.has_key('lang'):
      text = line['text']
      lang = line['lang']
      chars = len(text)
      print 'text : %s' % text
      print 'language : %s' % lang
      print '# of chars : %i' % chars
      if chars > maxChars:
        maxChars = chars
      print '--'*10
      count += 1
      if count >= 50:
        print 'maximumChars :  %i' % maxChars
        exit(1)
  except UnicodeEncodeError:
#    print line['lang']
#    f = open('data/error.log','a')
#    f.write(text)
    continue
  #except KeyError, httplib.IncompleteRead:
  #  continue

