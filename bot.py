# resources
import getopt
import sys
from xml.etree.ElementTree import parse

from telegram.ext import Updater, CommandHandler

import handlers
import logging

# configs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# opts handling
test_mode = False
argv = sys.argv[1:]
if len(argv) > 0:
    try:
        opts, args = getopt.getopt(argv, "", "testing")
    except getopt.GetoptError as err:
        print err
        sys.exit(2)

    for o, a in opts:
        if o == '--testing':
            test_mode = True
        else:
            assert False, "unhandled option"


# token import
config = parse('config.xml')
if test_mode is True:
    token = config.findtext('beta')
else:
    token = config.findtext('released')

updater = Updater(token=token)
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

wontattend_handler = CommandHandler('wontattend', handlers.wontattend, pass_args=False)
dispatcher.add_handler(wontattend_handler)

tentative_handler = CommandHandler('tentative', handlers.tentative, pass_args=False)
dispatcher.add_handler(tentative_handler)

list_handler = CommandHandler('list', handlers.showlist)
dispatcher.add_handler(list_handler)

# init
if __name__ == "__main__":
    updater.start_polling()
