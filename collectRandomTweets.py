#! /usr/bin/python
import getCredentials
status = getCredentials.api.GetStreamSample()


# start random streamer for the timeline
# this script does not end, has to be stopped manually.
# line is the entry for each tweet
# it is a python dictionary, for all the keys, check README file.

count = 0
maxChars = 0
listOfTweets = []
checkList = []
# every tweet is a python dictionary
# save tweets in a python list and check if every dictionary item has the
# the same structure
for tweet in status:
# listOfTweets.append(tweet)    
  tweetItems = len(tweet)
  #print tweetItems
  if tweetItems not in checkList:
    print tweetItems
    checkList.append(tweetItems)
    with open (str(tweetItems),'w') as f:
      for item in tweet:
        f.write(item+'\n')
  print '%ith tweet.....' % count 

 
  count += 1
  if count >= 1000:
    break


print len(listOfTweets)
#print listOfTweets[0]
