#!/usr/bin/python
import mysql

## some func
def makeUserDic(update):
    user = {'first_name': update.message.from_user.first_name, 'last_name': update.message.from_user.last_name,
            'username': update.message.from_user.username, 'user_id': update.message.from_user.id}
    return user


## handlers

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def krystian(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Krystian is a pussy who uses cheats (like TriggerBot, WH and, "
                                                         "of course, AimBot) to pretend, that he's somewhat better in"
                                                         " CS:GO than rest of his team")

def make(bot, update, args):
    name = ' '.join(args)
    chat_id = update.message.chat_id
    exists = mysql.checkListExistence(chat_id)
    if exists == True:
        text = "There is already created list. You have to close it first with /close"
        print "list exists"
    else:
        result = mysql.create_list(chat_id, name)
        if result == True:
            text = "List %s has been created succesfully!" % (name)
            print "list created"
        else:
            text = "Ups! Something went wrong :( Your list has not been created. Please contact MSokol00 on telegram"

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
    #TODO implement fime functionality, for now args not in use and time populated with NULL value
    chat_id = update.message.chat_id
    exists = mysql.checkListExistence(chat_id)
    if exists == True:
        user = makeUserDic(update)
        mysql.attend(chat_id,user,answer='will')
        text = u"{} {} will attend!".format(user['first_name'],user['last_name'])
    else:
        text = "There is no list to attend! Create one with /make"

    bot.sendMessage(chat_id=chat_id, text=text)

def wontattend(bot, update, args):
    #TODO implement fime functionality, for now args not in use and time populated with NULL value
    chat_id = update.message.chat_id
    exists = mysql.checkListExistence(chat_id)
    if exists == True:
        user = makeUserDic(update)
        mysql.attend(chat_id,user,answer='wont')
        text = u"{} {} won't attend!".format(user['first_name'],user['last_name'])
    else:
        text = "There is no list to attend! Create one with /make"

    bot.sendMessage(chat_id=chat_id, text=text)

def tentiative(bot, update, args):
    #TODO implement fime functionality, for now args not in use and time populated with NULL value
    chat_id = update.message.chat_id
    exists = mysql.checkListExistence(chat_id)
    if exists == True:
        user = makeUserDic(update)
        mysql.attend(chat_id,user,answer='tent')
        text = u"{} {} is tentative...".format(user['first_name'],user['last_name'])
    else:
        text = "There is no list to attend! Create one with /make"

    bot.sendMessage(chat_id=chat_id, text=text)