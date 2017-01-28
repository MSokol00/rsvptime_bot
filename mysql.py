#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     #passwd="megajonhy",  # your password
                     db="rsvptime_bot")        # name of the data base
cur = db.cursor()


## make list
def create_list(chat_id, name):
    sql = "INSERT INTO lists (chat_id, name) VALUES (%s, %s)" % (chat_id, name)
    print sql
    print chat_id
    print name
    #try:
    cur.execute(sql)
    db.commit()
    return True
    #except:
       # db.rollback()
      #  return False



