#!/usr/bin/python
import mysql

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def krystian(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Krystian is a pussy who uses cheats (like TriggerBot, WH and, "
                                                         "of course, AimBot) to pretend, that he's somewhat better in"
                                                         " CS:GO than rest of his team")

def make(bot, update, args):
    name = ''.join(args)
    chat_id = update.message.chat_id
    exists = mysql.check_list_existence(chat_id)
    if exists == True:
        text = "There is already created list. You have to close it first with /close"
        if debug == True:
            print "list exists"
    else:
        result = mysql.create_list(chat_id, name)
        if result == True:
            text = "List %s has been created succesfully!" % (name)
            if debug == True:
                print "list created"
        else:
            text = "Ups! Something went wrong :( Your list has not been created. Please contact MSokol00 on telegram"

    bot.sendMessage(chat_id=chat_id, text=text)