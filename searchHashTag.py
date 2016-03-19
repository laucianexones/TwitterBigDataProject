#! /usr/bin/python
# -*- coding: utf-8 -*-
import getCredentials 
import time

#f = open('search_hashtag','w')
hashtag = '#AbdülHamidiAnlamak'
hashtag = hashtag.decode('utf-8')

f = open('search_hashtag','w')
tweets = getCredentials.api.GetSearch(hashtag, count=100)
for t in tweets:
  tweet = t.text
  try:
    tweet = tweet.encode('utf-8')
    f.write('%s\n' % tweet)
    f.write('----\n')
  except UnicodeDecodeError,UnicodeEncodeError:
    continue
f.close()
