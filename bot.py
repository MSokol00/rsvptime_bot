# resources
from telegram.ext import Updater, CommandHandler
import handlers, logging, sys

# configs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token="308560134:AAGxr4JKMCj-vGKdIPZKvOT51Sf8UPW837o")
dispatcher = updater.dispatcher

def if_debug():
    if len(sys.argv) >= 1:
        if sys.argv[0] == 'debug': debug = True
        global debug

# command handlers
start_handler = CommandHandler('start', handlers.start)
dispatcher.add_handler(start_handler)

krystian_handler = CommandHandler('krystian', handlers.krystian)
dispatcher.add_handler(krystian_handler)

make_handler = CommandHandler('make', handlers.make, pass_args=True)
dispatcher.add_handler(make_handler)

# init
if __name__ == "__main__":
    if_debug()
    updater.start_polling()