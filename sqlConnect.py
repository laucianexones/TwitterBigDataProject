#!/usr/bin/python

import MySQLdb
# TODO read credentials from a file/database
try:
  db = MySQLdb.connect(host='', \
                       user='', \
                       passwd='$$l', \
                       db = 'twitter_db')
  

# TODO global except is too dangerous
# better handling of the error 
except:
  exit(1)


#print db
#print type(db)

#cur = db.cursor()
#cur.execute('select * from deneme')
#
#db.close()
