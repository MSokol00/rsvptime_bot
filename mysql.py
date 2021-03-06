#!/usr/bin/python
# noinspection PyUnresolvedReferences
import MySQLdb


def getListId(chat_id):
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    sql = u"SELECT id FROM lists WHERE chat_id = {}".format(unicode(str(chat_id)))
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
    sql = u"SELECT name FROM lists WHERE chat_id = {}".format(unicode(str(chat_id)))
    cur.execute(sql)
    list_name_cur = cur.fetchone()
    list_name = u''.join(list_name_cur[0])
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
    sql = "SELECT r.answer_id, u.first_name, u.last_name, u.user_name, r.time " \
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
    sql = u"SELECT user_id FROM users WHERE user_id = '{}'".format(unicode(str(user_id)))
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


def addRSVP(list_id, user_id, answer_id, time='NULL'):
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset
    cur = db.cursor()

    print "addRSVP: list_id", list_id, ";user_id:", user_id, ";answer_id:", answer_id, ";time:", time
    if time == 'NULL':
        sql = "INSERT INTO rsvp (time, list_id, user_id, answer_id) VALUES ({}, '{}', '{}', '{}')".format(
            time, list_id, user_id, answer_id)
    else:
        sql = "INSERT INTO rsvp (time, list_id, user_id, answer_id) VALUES ('{}', '{}', '{}', '{}')".format(
            time, list_id, user_id, answer_id)
    print sql
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()


def updateRSVP(list_id, user_id, answer_id, time='NULL'):
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()

    print "updateRSVP: list_id", list_id, ";user_id:", user_id, ";answer_id:", answer_id, "time:", time
    if time == 'NULL':
        sql = "UPDATE rsvp SET time = {}, answer_id = '{}' WHERE list_id = '{}' and user_id = '{}'".format(
            time, answer_id, list_id, user_id)
    else:
        sql = "UPDATE rsvp SET time = '{}', answer_id = '{}' WHERE list_id = '{}' and user_id = '{}'".format(
            time, answer_id, list_id, user_id)
    print sql
    cur.execute(sql)
    db.commit()
    cur.close()
    db.close()


def checkRSVP(list_id, user_id, answer_id, time='NULL'):
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    if time is None:
        time = 'NULL'
    sql = "SELECT answer_id, time FROM rsvp WHERE list_id = '{}' and user_id = '{}'".format(list_id, user_id)
    cur.execute(sql)
    result = cur.fetchone()
    if result is None:
        addRSVP(list_id=list_id, user_id=user_id, answer_id=answer_id, time=time)
    elif result is not None and (int(result[0]) != answer_id or result[1] != time):
        updateRSVP(list_id=list_id, answer_id=answer_id, user_id=user_id, time=time)


# make list
def create_list(chat_id, name):
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         # passwd="megajonhy",  # your password
                         db="rsvptime_bot",  # name of the data base
                         charset='utf8')  # overwrites default charset

    cur = db.cursor()
    sql = u"INSERT INTO lists (chat_id, name) VALUES ({}, '{}')".format(chat_id, name)
    # noinspection PyBroadException
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


def attend(chat_id, user, answer, time='NULL'):
    list_id = getListId(chat_id)
    if not checkUserExistence(user['user_id']):
        addUser(user)
    answer_ids = {
        'will': 1,
        'wont': 2,
        'tent': 3
    }
    print "attend: answer:", answer
    answer_id = answer_ids.get(answer)
    checkRSVP(list_id=list_id, user_id=user['user_id'], answer_id=answer_id, time=time)


def getListRSVP(chat_id):
    list_id = getListId(chat_id)
    list_name = getListName(chat_id)
    attendees = getAttendees(list_id)
    list_obj = {
        'listName': list_name,
        'users': attendees
    }
    return list_obj
