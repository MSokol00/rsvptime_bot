# resources
from telegram.ext import Updater, CommandHandler
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
    bot.sendMessage(chat_id=update.message.chat_id, text="Krystian is pussy who uses cheats (like TriggerBot, WH and, of course, AimBot, to pretend, that he's somewhat better in CS than rest of his team")

start_handler = CommandHandler('Krystian', start)
dispatcher.add_handler(start_handler)

# init
if __name__ == "__main__":
    updater.start_polling()