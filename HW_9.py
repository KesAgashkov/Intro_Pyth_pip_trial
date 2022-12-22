import time
from random import randint
from colorama import init, Fore,Back
init()

from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler
from telegram import Update
from anecAPI import anecAPI
from config import TOKEN
import datetime
from log import log



# 1.Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

# def game_cross_zero():
#     area = [
#         ['*', '*', '*'],
#         ['*', '*', '*'],
#         ['*', '*', '*']
#     ]
#     print(Fore.CYAN +'Добро пожаловать в игру "Крестики-Нолики')
#     print(Fore.LIGHTMAGENTA_EX + 'Киньте монетку, чтобы определить очередность или выберите число от 1 до 2: \n')
#     time.sleep(1)
#     print('Готовы?\n')
#     time.sleep(2)
#     print(f'       {randint(1,2)}\n')
#     for item in area:
#         print(Fore.RED + f'{item}\n')
#
#     while True:
#         fir1, fir2 = map(int, input(Fore.BLUE + 'Первый игрок. Напиши номер строки и столбца через пробел (1-3),'
#                                     'где хочешь поставить "X"(Счёт идёт с левого верхнего угла):').split())
#         fir1 = int(fir1 - 1)
#         fir2 = int(fir2 - 1)
#         if fir1 in [0, 1, 2] and fir2 in [0, 1, 2] and area[fir1][fir2] != "X" and area[fir1][fir2] != "0":
#             area[fir1][fir2] = "X"
#             for item in area:
#                 print(Fore.RED + f'{item}\n')
#         else:
#             print(Fore.BLUE+'Вы ввели неверные значения, попробуйте заново')
#             continue
#         if (area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X') or \
#                 (area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X') or \
#                 (area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X') or \
#                 (area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X') or \
#                 (area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X') or \
#                 (area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X') or \
#                 (area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X') or \
#                 (area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X'):
#             str1 = 'Победил Первый игрок. Поздравляю'
#             return str1
#             break
#
#         sec1, sec2 = map(int, input(Fore.BLUE + 'Второй игрок. Напиши номер строки и столбца через пробел (1-3),'
#                                         'где хочешь поставить "0"(Счёт идёт с левого верхнего угла):').split())
#         sec1 = int(sec1 - 1)
#         sec2 = int(sec2 - 1)
#         if sec1 in [0, 1, 2] and sec2 in [0, 1, 2] and area[sec1][sec2] != "X" and area[sec1][sec2] != "0":
#             area[sec1][sec2] = "0"
#             for item in area:
#                 print(Fore.RED + f'{item}\n')
#         if (area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0') or \
#                 (area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0') or \
#                 (area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0') or \
#                 (area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0') or \
#                 (area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0') or \
#                 (area[0][2] == '0' and area[1][2] == '0' and area[2][2] == '0') or \
#                 (area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0') or \
#                 (area[0][2] == '0' and area[1][1] == '0' and area[2][0] == '0'):
#             str2 = 'Победил Второй игрок. Поздравляю'
#             return str2
#         else:
#             print('Вы ввели неверные значения, попробуйте заново, ход переходит сопернику')
#             continue
#
# print(Fore.YELLOW + game_cross_zero())

# 2.Прикрутить бота к задачам с предыдущего семинара: Создать калькулятор для работы с
# рациональными и комплексными числами, организовать меню, добавив в него систему логирования


def get_info(update: Update, context: CallbackContext):
    log(update, context)
    after_command = context.args
    print(after_command)
    update.message.reply_text("Приветствую.Вы зашли в калькулятор.\n Я могу совершать операции с двумя целыми числами\n "
                              "Мат операции совершаются не более чем с двумя числами. ввод идё в одну строку(команда и значения через пробел)"
                              "Вычитание - команда '/minus'; Сложение - команда '/plus'; Умножение - команда '/mult'; деление - команда '/div'\n"
                              "Вывод времени - команды '/time'")

def plus_info(update: Update, context: CallbackContext):
    log(update,context)
    text = update.message.text
    items =  text.split()
    x  = int(items[1])
    y = int(items[2])
    update.message.reply_text(f"{x} + {y} = {x+y}")



def minus_info(update: Update, context: CallbackContext):
    log(update, context)
    text = update.message.text
    items = text.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f"{x} - {y} = {x - y}")


def mult_info(update: Update, context: CallbackContext):
    log(update, context)
    text = update.message.text
    items = text.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f"{x} * {y} = {x * y}")

def div_info(update: Update, context: CallbackContext):
    log(update, context)
    text = update.message.text
    items = text.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f"{x} / {y} = {round((x / y),2)}")

def get_time(update: Update, context: CallbackContext):
    update.message.reply_text(f"{datetime.datetime.now().time()}")
    log(update, context)

def get_message(update: Update, context: CallbackContext):
    log(update, context)
    message = update.message.text
    print(message)
    if 'приве' in message:
        update.message.reply_text(f'Здравствуйте {update._effective_user.first_name}!')
        return None
    update.message.reply_text(f'Я вас не понимаю, введите команду /info')


updater = Updater(TOKEN)
dispetcher = updater.dispatcher


info_handler = CommandHandler('info', get_info)
plus_handler = CommandHandler('plus', plus_info)
minus_handler = CommandHandler('minus', minus_info)
mult_handler = CommandHandler('mult', mult_info)
div_handler = CommandHandler('div', div_info)
time_handler = CommandHandler('time', get_time)
message_handler = MessageHandler(Filters.text, get_message)



dispetcher.add_handler(info_handler)
dispetcher.add_handler(plus_handler)
dispetcher.add_handler(minus_handler)
dispetcher.add_handler(mult_handler)
dispetcher.add_handler(div_handler)
dispetcher.add_handler(time_handler)
dispetcher.add_handler(message_handler)



print('сервер запущен')
updater.start_polling()
updater.idle()