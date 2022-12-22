from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler
from telegram import Update
import datetime


def log(update: Update, context: CallbackContext):
    with open('log.csv', 'a') as file:
        file.write(f'{datetime.datetime.now().time()}|{update.effective_user.first_name}|{update.effective_user.id}|'
                   f'{update.message.text}\n')
