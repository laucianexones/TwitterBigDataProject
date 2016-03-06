#! /usr/bin/python

import twitter

with open('credentials','r') as credentialsFile:
   lines = credentialsFile.readlines()

api = twitter.Api( 
  access_token_key = str(lines[0]).rstrip(), \
  access_token_secret = str(lines[1]).rstrip(), \
  consumer_key = str(lines[2]).rstrip(), \
  consumer_secret = str(lines[3]).rstrip()\
)

cred_dict = api.VerifyCredentials()
print cred_dict
