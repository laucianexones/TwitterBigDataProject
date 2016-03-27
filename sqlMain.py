#! /usr/bin/python

import sqlConnect as sqlc

def selectAll(cur):
  # type: (object) -> object
  cur.execute('select * from deneme')
  for row in cur.fetchall():
    print row


def insertInto(cur):
  command = 'insert into deneme (id_deneme, tweet) values (6, \'blaa bluuub\')'
  cur.execute(command)


def deleteFrom():
  # delete from twitter_db.deneme where id_deneme = 4
  pass

def clearDB(cur):
  keys = []
  cur.execute('select * from deneme')
  for row in cur.fetchall():
    keys.append(row[0])

  for i in keys:
    command = 'delete from deneme where id_deneme = %s' %i
    cur.execute(command)



if __name__ == '__main__':
  if not sqlc.db:
    exit(1)

  cur = sqlc.db.cursor()

  print 'listing deneme table'
  selectAll(cur)
  print '-'*20

  print 'inserting 6, bla blub to the deneme table'
  insertInto(cur)
  print '-' * 20

  print 'listing deneme table'
  selectAll(cur)
  print '-' * 20

  print 'clearing the deneme table'
  clearDB(cur)
  print '-' * 20

  print 'listing deneme table'
  selectAll(cur)
  print '-' * 20

  sqlc.db.commit()
  sqlc.db.close()

