#! /usr/bin/python
import twitter
import os

# define where to find the credentials file
home = os.path.expanduser('~')
default_file = '.credentials'
credentials_file = os.path.join(home, default_file)

# check if the credentials file exists
if not os.path.isfile(credentials_file):
  print 'credentials file %s not found..exiting' % credentials_file
  exit(1)

with open(credentials_file, 'r') as credentialsFile:
   lines = credentialsFile.readlines()

api = twitter.Api( 
  access_token_key = str(lines[0]).rstrip(), \
  access_token_secret = str(lines[1]).rstrip(), \
  consumer_key = str(lines[2]).rstrip(), \
  consumer_secret = str(lines[3]).rstrip()\
)

cred_dict = api.VerifyCredentials()
if not cred_dict:
  print 'Problem..check your credentials..exiting'
  exit(1)
