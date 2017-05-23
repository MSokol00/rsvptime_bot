#!/usr/bin/python
import mysql
import re
import datetime


## some func
def makeUserDic(update):
    user = {'first_name': update.message.from_user.first_name, 'last_name': update.message.from_user.last_name,
            'username': update.message.from_user.username, 'user_id': update.message.from_user.id}
    return user


def emojiAnswer(answer_id):
    emoji = {
        '1': u'\u2705',  # willattend
        '2': u'\u274C',  # wontattend
        '3': u'\U0001F414'  # tentative
    }
    answer = str(int(answer_id))
    return emoji[answer]


def buildListText(list, status):
    if status == 'open':
        title = u"On the list for '{}': \n \n".format(list['listName'])
    elif status == 'close':
        title = u"List '{}' closed! Final results: \n \n".format(list['listName'])
    print list
    wi_i = 1
    wo_i = 1
    t_i = 1

    will_attend = u''
    wont_attend = u''
    tent = u''
    for tuple in list['users']:
        emoji = emojiAnswer(tuple[0])
        # time -----------------------------------------
        if tuple[4] != 'NULL' and tuple[4] is not None:
            print "line 40: tuple[4]:", tuple[4]
            time = stringToTime(tuple[4])
            print "line 42: time:", time
            time_str = " "+u"\u231A"+" {:%H:%M}".format(time)
            print "line 44: time_str:", time_str
        else:
            time_str = ""
        # time -----------------------------------------
        if int(tuple[0]) == 1:
            will_attend = will_attend + unicode(str(wi_i)) + u'.' + emoji + u' ' + tuple[1] + u' ' + tuple[
                2] + time_str + u'\n'
            wi_i += 1
        elif int(tuple[0]) == 2:
            wont_attend = wont_attend + unicode(str(wo_i)) + u'.' + emoji + u' ' + tuple[1] + u' ' + tuple[
                2] + time_str + u'\n'
            wo_i += 1
        elif int(tuple[0]) == 3:
            tent = tent + unicode(str(t_i)) + u'.' + emoji + u' ' + tuple[1] + u' ' + tuple[
                2] + time_str + u'\n'
            t_i += 1
    if will_attend.replace(" ", "") != "": will_attend += u'\n'
    if wont_attend.replace(" ", "") != "": wont_attend += u'\n'
    if tent.replace(" ", ""): tent += u'\n'
    text = title + will_attend + tent + wont_attend
    return text


def stringToTime(string):
    try:
        time_obj = re.split(":", string)
        print "time_obj in stringToTime:", time_obj
        time = datetime.time(int(time_obj[0]), int(time_obj[1]), 00)
        print "time in stringToTime:", time
    except:
        time = None
    return time


## handlers

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
    #TODO change that shit to make something usefull, like help


def krystian(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Krystian is a pussy who uses cheats (like TriggerBot, WH and, "
                         "of course, AimBot) to pretend, that he's somewhat better in"
                         " CS:GO than rest of his team")


def make(bot, update, args):
    name = u' '.join(args)
    # debug
    print name.encode('utf-8')
    # /debug
    chat_id = update.message.chat_id

    # check if list already exists in chat
    exists = mysql.checkListExistence(chat_id)
    if exists == True:
        text = "There is already created list. You have to close it first with /close"
        print "list exists"
    else:
        if name.replace(" ", "") != "":
            result = mysql.create_list(chat_id, name)
            if result == True:
                text = "List %s has been created succesfully!" % (name)
                print "list created"
            else:
                text = "Ups! Something went wrong :( Your list has not been created. Please contact MSokol00 on telegram"
        else:
            text = "Why don't You give a name for Your list? Try '/make noobs gathering'"

    bot.sendMessage(chat_id=chat_id, text=text)


def close(bot, update):
    chat_id = update.message.chat_id
    exists = mysql.checkListExistence(chat_id)
    if exists == True:
        mysql.close_list(chat_id)
        print "list closed"
        text = "List closed succesfully!"
    else:
        text = "There is no list to close! You have to first create one with /make"

    bot.sendMessage(chat_id=chat_id, text=text)


def willattend(bot, update, args):

    # time section -----------------------------------------
    text_time = u''
    time = None
    if len(args) != 0:
        print args[0]

        if re.match("[0-9]{2}:[0-9]{2}", args[0]) :
            time = stringToTime(args[0])
            if time is None:
                text_time = u"Nice try with time :)"
                print text_time
        else:
            text_time = u"Given time is wrong however. Inform about time of Your arrival with: /willattend 16:45."
            print text_time
    # /time section ----------------------------------------
    chat_id = update.message.chat_id
    exists = mysql.checkListExistence(chat_id)
    if exists:
        user = makeUserDic(update)
        mysql.attend(chat_id, user, answer='will', time=time)
        if time is not None:
            text = u"{} {} will attend at {:%H:%M}!".format(user['first_name'], user['last_name'], time)
        else:
            text = u"{} {} will attend!".format(user['first_name'], user['last_name'])+u" "+text_time
        text = text.replace('None ', '')
    else:
        text = u"There is no list to attend! Create one with /make"

    bot.sendMessage(chat_id=chat_id, text=text)


def wontattend(bot, update, args):
    chat_id = update.message.chat_id
    exists = mysql.checkListExistence(chat_id)
    if exists == True:
        user = makeUserDic(update)
        mysql.attend(chat_id, user, answer='wont')
        text = u"{} {} won't attend!".format(user['first_name'], user['last_name'])
        text = text.replace('None ', '')
    else:
        text = "There is no list to attend! Create one with /make"

    bot.sendMessage(chat_id=chat_id, text=text)


def tentative(bot, update, args):
    chat_id = update.message.chat_id
    exists = mysql.checkListExistence(chat_id)
    if exists == True:
        user = makeUserDic(update)
        mysql.attend(chat_id, user, answer='tent')
        text = u"{} {} is tentative...".format(user['first_name'], user['last_name'])
        text = text.replace('None ', '')
    else:
        text = "There is no list to attend! Create one with /make"

    bot.sendMessage(chat_id=chat_id, text=text)


def list(bot, update):
    #TODO time
    chat_id = update.message.chat_id
    exists = mysql.checkListExistence(chat_id)
    if exists == True:
        list = mysql.getListRSVP(chat_id)
        text = buildListText(list, 'open')
    else:
        text = "There is no list. You should create one with /make"

    bot.sendMessage(chat_id=chat_id, text=text)
