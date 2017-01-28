#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     #passwd="megajonhy",  # your password
                     db="rsvptime_bot")        # name of the data base
cur = db.cursor()

def check_list_existence(chat_id):
    sql = "SELECT 1 as 'result' FROM lists WHERE chat_id = %s" % (chat_id)
    cur.execute(sql)
    result = cur.fetchone()
    if result[0] == '1': exist = True
    else: exist = False
    return exist

## make list
def create_list(chat_id, name):
    sql = "INSERT INTO lists (chat_id, name) VALUES (%s, '%s')" % (chat_id, name)
    try:
        cur.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
        return False



