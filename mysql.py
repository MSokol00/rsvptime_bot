#!/usr/bin/python
import MySQLdb


def getListId(chat_id):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    sql = "SELECT id FROM lists WHERE chat_id = %s" % (chat_id)
    cur.execute(sql)
    list_id = cur.fetchone()
    if list_id is not None:
        list_id = int(list_id[0])
    cur.close()
    db.close()
    return list_id

def getListName(chat_id):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    sql = "SELECT name FROM lists WHERE chat_id = %s" % (chat_id)
    cur.execute(sql)
    list_name_cur = cur.fetchone()
    list_name = u''
    list_name += str(list_name_cur[0])
    cur.close()
    db.close()
    return list_name

def getAttendees(list_id):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    sql = "SELECT r.answer_id, u.first_name, u.last_name, u.user_name " \
          "FROM rsvp r INNER JOIN users u on r.user_id = u.user_id " \
          "WHERE r.list_id = '{}'".format(list_id)
    cur.execute(sql)
    attendees = cur.fetchall()
    cur.close()
    db.close()
    return attendees

def checkListExistence(chat_id):
    result = getListId(chat_id)
    if result is not None:
        exist = True
    else:
        exist = False
    return exist

def checkUserExistence(user_id):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    sql = "SELECT user_id FROM users WHERE user_id = '%s'" % (user_id)
    cur.execute(sql)
    result = cur.fetchone()
    if result is not None:
        exist = True
    else:
        exist = False
    cur.close()
    db.close()
    return exist

def addUser(user):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    sql = u"INSERT INTO users (user_id, first_name, last_name, user_name) VALUES ('{}', '{}', '{}', '{}')".format(
        user['user_id'], user['first_name'], user['last_name'], user['username'])
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()

def addRSVP(list_id, user_id, answer_id, time=None):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    #TODO time functionality

    print "addRSVP: list_id",list_id,";user_id:",user_id,";answer_id:",answer_id
    sql = "INSERT INTO rsvp (time, list_id, user_id, answer_id) VALUES (NULL, '{}', '{}', '{}')".format(
        list_id, user_id, answer_id)
    print sql
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()

def updateRSVP(list_id, user_id, answer_id, time=None):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    # TODO time functionality

    print "updateRSVP: list_id", list_id, ";user_id:", user_id, ";answer_id:", answer_id
    sql = "UPDATE rsvp SET time = NULL, answer_id = '{}' WHERE list_id = '{}' and user_id = '{}'".format(answer_id,list_id,user_id)
    print sql
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()

def checkRSVP(list_id, user_id, answer_id, time=None):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    sql = "SELECT answer_id FROM rsvp WHERE list_id = '{}' and user_id = '{}'".format(list_id,user_id)
    cur.execute(sql)
    result = cur.fetchone()
    if result is None:
        addRSVP(list_id=list_id, user_id=user_id, answer_id=answer_id)
    elif result is not None and int(result[0]) != answer_id:
        updateRSVP(list_id=list_id, answer_id=answer_id, user_id=user_id, time=None)

## make list
def create_list(chat_id, name):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    sql = u"INSERT INTO lists (chat_id, name) VALUES ({}, '{}')".format(chat_id, name)
    try:
        cur.execute(sql)
        db.commit()
        cur.close()
        db.close()
        return True
    except:
        db.rollback()
        cur.close()
        db.close()
        return False

def close_list(chat_id):

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    sql = "DELETE FROM lists WHERE chat_id = {}".format(chat_id)
    print sql
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()

def attend(chat_id, user, answer):
    list_id = getListId(chat_id)
    if checkUserExistence(user['user_id']) == False:
        addUser(user)
    answer_ids = {
        'will': 1,
        'wont': 2,
        'tent': 3
    }
    print "attend: answer:",answer
    answer_id = answer_ids.get(answer)
    checkRSVP(list_id=list_id,user_id=user['user_id'],answer_id=answer_id)

def getListRSVP(chat_id):
    list_id = getListId(chat_id)
    listName = getListName(chat_id)
    attendees = getAttendees(list_id)
    list = {
        'listName': listName,
        'users': attendees
    }
    return list




