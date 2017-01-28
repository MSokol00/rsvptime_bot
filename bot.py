# resources
from telegram.ext import Updater, CommandHandler
import mysql
import logging


# configs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token="308560134:AAGxr4JKMCj-vGKdIPZKvOT51Sf8UPW837o")
dispatcher = updater.dispatcher


# command handlers
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def krystian(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Krystian is a pussy who uses cheats (like TriggerBot, WH and, "
                                                         "of course, AimBot) to pretend, that he's somewhat better in"
                                                         " CS:GO than rest of his team")

krystian_handler = CommandHandler('krystian', krystian)
dispatcher.add_handler(krystian_handler)


def make(bot, update, args):
    name = ''.join(args)
    chat_id = update.message.chat_id
    exists = mysql.check_list_existence(chat_id)
    if exists == True:
        text = "There is already created list. You have to close it first with \/close"
        print "list exists"
    else:
        result = mysql.create_list(chat_id, name)
        if result == True:
            text = "List %s has been created succesfully!" % (name)
            print "list created"
        else:
            text = "Ups! Something went wrong :( Your list has not been created. Please contact MSokol00 on telegram"

    bot.sendMessage(chat_id=chat_id, text=text)

make_handler = CommandHandler('make', make, pass_args=True)
dispatcher.add_handler(make_handler)

# init
if __name__ == "__main__":
    updater.start_polling()