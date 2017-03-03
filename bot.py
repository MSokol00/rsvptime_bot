# resources
from telegram.ext import Updater, CommandHandler
import handlers, logging

# configs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token="308560134:AAGxr4JKMCj-vGKdIPZKvOT51Sf8UPW837o")
dispatcher = updater.dispatcher

# command handlers
start_handler = CommandHandler('start', handlers.start)
dispatcher.add_handler(start_handler)

krystian_handler = CommandHandler('krystian', handlers.krystian)
dispatcher.add_handler(krystian_handler)

make_handler = CommandHandler('make', handlers.make, pass_args=True)
dispatcher.add_handler(make_handler)

close_handler = CommandHandler('close', handlers.close)
dispatcher.add_handler(close_handler)

willattend_handler = CommandHandler('willattend', handlers.willattend, pass_args=True)
dispatcher.add_handler(willattend_handler)

wontattend_handler = CommandHandler('wontattend', handlers.wontattend, pass_args=True)
dispatcher.add_handler(wontattend_handler)

tentative_handler = CommandHandler('tentative', handlers.tentatve, pass_args=True)
dispatcher.add_handler(tentative_handler)

list_handler = CommandHandler('list', handlers.list)
dispatcher.add_handler(list_handler)

# init
if __name__ == "__main__":
    updater.start_polling()