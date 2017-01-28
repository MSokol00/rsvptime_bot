#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     #passwd="megajonhy",  # your password
                     db="rsvptime_bot")        # name of the data base


def check_list_existence(chat_id):
    cur = db.cursor()
    sql = "SELECT 'yes' as 'result' FROM lists WHERE chat_id = %s" % (chat_id)
    cur.execute(sql)
    ########
    print "####existence sql: \n"+str(sql)+"\n ________________"
    ########
    result = cur.fetchone()
    #######
    print "####result of existence: \n"
    print result
    print result[0]
    print "____________________________"
    ########
    if result[0] == 'yes': exist = True
    else: exist = False
    ########
    print exist
    ########
    cur.close()
    return exist

## make list
def create_list(chat_id, name):
    cur = db.cursor()
    sql = "INSERT INTO lists (chat_id, name) VALUES (%s, '%s')" % (chat_id, name)
    try:
        cur.execute(sql)
        db.commit()
        cur.close()
        return True
    except:
        db.rollback()
        cur.close()
        return False



