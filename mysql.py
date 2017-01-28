#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     #passwd="megajonhy",  # your password
                     db="rsvptime_bot")        # name of the data base


def getListId(chat_id):
    cur = db.cursor()
    sql = "SELECT id FROM lists WHERE chat_id = %s" % (chat_id)
    cur.execute(sql)
    list_id = cur.fetchone()
    if list_id is not None:
        list_id = int(list_id[0])
    cur.close()
    return list_id

def checkListExistence(chat_id):
    result = getListId(chat_id)
    #######
    print "####result of existence: \n", result, "____________________________"

    if result is not None:
        exist = True
    else:
        exist = False

    print exist
    return exist

def checkUserExistence(user_id):
    cur = db.cursor()
    sql = "SELECT id FROM users WHERE user_id = %s" % (user_id)
    cur.execute(sql)
    result = cur.fetchone()
    if result is not None:
        exist = True
    else:
        exist = False
    cur.close()
    return exist

def addUser(user):
    cur = db.cursor()
    sql = "INSERT INTO users (user_id, first_name, last_name, user_name) VALUES ('{}', '{}', '{}', '{}')".format(
        user['user_id'], user['first_name'], user['last_name'], user['username'])
    cur.execute(sql)
    db.commit()
    cur.close()

def addRSVP(list_id, user_id, answer_id, time=None):
    cur = db.cursor()
    #TODO time functionality
    sql = "INSER INTO rsvp (time, list_id, user_id, answer_id) VALUES (NULL, '{}', '{}', '{}')".format(
        list_id, user_id, answer_id)
    cur.execute(sql)
    db.commit()
    cur.close()

## make list
def create_list(chat_id, name):
    cur = db.cursor()
    sql = "INSERT INTO lists (chat_id, name) VALUES ({}, '{}')".format(chat_id, name)
    try:
        cur.execute(sql)
        db.commit()
        cur.close()
        return True
    except:
        db.rollback()
        cur.close()
        return False

def close_list(chat_id):
    cur = db.cursor()
    sql = "DELETE FROM lists WHERE chat_id = {}".format(chat_id)
    print sql
    cur.execute(sql)
    db.commit()
    cur.close()

def attend(chat_id, user, answer):
    list_id = getListId(chat_id)
    if checkUserExistence(user['user_id']) == False:
        addUser(user)
    answer_ids = {
        'will': 1,
        'wont': 2,
        'tent': 3
    }
    answer_id = answer_ids.get(answer)
    addRSVP(list_id=list_id,user_id=user['user_id'],answer_id=answer_id)




