import daemon

from spam import do_main_program

with daemon.DaemonContext():
    do_main_program()
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update


updater = Updater("5666296465:AAEWRFKxrFiKi8RLlCZweRRvy9zLHoRNrJ4",
                  use_context=True)


dispatcher: Dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    """
    the callback for handling start command
    """

    bot: Bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="به ربات تلگرامی چنل @snowcinema خوش آمدید\n\n\nاگر پیشنهاد انتقاد یا درخواستی دارید لطفا اعلام کنید")

dispatcher.add_handler(
    CommandHandler("start", start))

def echo(update: Update, context: CallbackContext):
    """
    the callback for handling echo command
    """

    bot: Bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="https://t.me/+fbO6I1VKJzZmNjE0")

dispatcher.add_handler(
    CommandHandler("ozviat", echo))

def echo(update: Update, context: CallbackContext):
    """
    the callback for handling echo command
    """

    bot: Bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id,
                     text="لطفا اسم فیلم و درخواستی خود را بنویسید")

dispatcher.add_handler(
    CommandHandler("darkhast", echo))




updater.start_polling()