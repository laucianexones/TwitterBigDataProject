#! /usr/bin/python

import twitter

with open('/home/kerem/.credentials','r') as credentialsFile:
   lines = credentialsFile.readlines()

api = twitter.Api( 
  access_token_key = str(lines[0]).rstrip(), \
  access_token_secret = str(lines[1]).rstrip(), \
  consumer_key = str(lines[2]).rstrip(), \
  consumer_secret = str(lines[3]).rstrip()\
)

cred_dict = api.VerifyCredentials()
if cred_dict:
  print 'Credentials OK..\n'
#print cred_dict

#users = api.GetFriends()
#for user in users:
#  print user

status = api.GetStreamSample()

for line in status:
  try:
    print line
    print '--'*10
  except KeyError, httplib.IncompleteRead:
    continue

