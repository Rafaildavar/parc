import pandas
import telebot
import os
from telebot import types
import time
from bs4 import BeautifulSoup
import requests as req


class Table:
    """Working table"""
    def __init__(self, table_location):
        self.table_sheet = "list_1"
        self.data_save_dict = {"user_name": None, "date": None, "weight_us": None, "push_up_use": None,
                               "squats_us": None, "plank_us": None, "twisting_us": None, "calories": None,
                               "activity time": None, "train_type": None, "k_train": None}

        self.time = None
        self.table = pandas.read_excel(table_location, sheet_name="list_1").to_dict("list")

    def new_user_add(self, data):
        """Aad new user in table"""
        self.table[data["user_name"]] = [self.data_save_dict["date"], self.data_save_dict["weight_us"],
                                         self.data_save_dict["push_up_use"], self.data_save_dict["squats_us"],
                                         self.data_save_dict["plank_us"], self.data_save_dict["twisting_us"],
                                         self.data_save_dict["k_train"], self.data_save_dict["train_type"], "#"]

    def save(self):
        print(self.table)
        writer = pandas.ExcelWriter("Table.xlsx", engine='xlsxwriter')
        save_sheet = pandas.DataFrame.from_dict(self.table, orient="index")
        save_sheet = save_sheet.transpose()
        save_sheet.to_excel(writer, sheet_name="list_1", index=False)
        writer.close()

    def read_data(self):
        """Reading data from table"""
        pass


table = Table("Table.xlsx")

t_start = time.ctime().split()[-2].split(':')[1], time.ctime().split()[-2].split(':')[2]
t_next = time.ctime().split()[-2].split(':')[1], time.ctime().split()[-2].split(':')[2]
# выведет первые 3 буквы дня недели
t = time.ctime().split()[0]
t = time.ctime()[0]
t = time.ctime().split()[0]


Sunday = [x[:-2] for  i in range(10) for x in open('message.txt')]
Monday = [x[:-2] for  i in range(10) for x in open('message.txt')]
Tuesday = [x[:-2] for  i in range(10) for x in open('message.txt')]
Wednesday = [x[:-2] for  i in range(10) for x in open('message.txt')]
Thursday = [x[:-2] for  i in range(10) for x in open('message.txt')]
Friday = [x[:-2] for  i in range(10) for x in open('message.txt')]
Saturday = [x[:-2] for  i in range(10) for x in open('message.txt')]
Sunday_slimming = []
Monday_slimming = []
Tuesday_slimming = []
Wednesday_slimming = []
Thursday_slimming = []
Friday_slimming = []
Saturday_slimming = []
cur = 0
cycle = 0

Sunday_g = []
Monday_g = []
Tuesday_g = []
Wednesday_g = []
Thursday_g = []
Friday_g = []
Saturday_g = []
cur_g = 0
cycle_g = 0


weekdays_slimming = {'Mon': [Monday_slimming, Monday_g],
                     'Tue': [Tuesday_slimming, Tuesday_g],
                     'Wed': [Wednesday_slimming, Wednesday_g],
                     'Thu': [Thursday_slimming, Thursday_g],
                     'Fri': [Friday_slimming, Friday_g],
                     'Sat': [Saturday_slimming, Saturday_g],
                     'Sun': [Sunday_slimming, Sunday_g]}

def try_int(string):
    for letter in string:
        if letter not in '0123456789':
            return False

    return True


a = time.ctime().split()[1:-1]
start = {'month': a[1],'time':a[2]}

def check_tr_time(Time):
    if Time == '09:00:00':
        return 1
    return 0


def check_notif_time(Time):
    if Time == '08:00:00':
        return 1
    return 0


if check_tr_time(start.get('time')):
    send_message = 'сегодняшняя тренировка'
if check_notif_time(start.get('time')):
    send_message = 'сегодняшняя тренировка начнется через час'





token = "6415654154:AAFyEgPIkc7EmppYMg0QCHHNn0Kmzlg3PCo"
bot = telebot.TeleBot(token)

k_train = 1.3
line = 0


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Введите имя ползователя ")
        bot.register_next_step_handler(message, weight)

    elif message.text == "/train":
        if table.table[7] == "low":
            chse_Exercises(message)
        if table.table[7] == "hard":
            filling_method(message)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Введите '/start', чтоб редактировать профиль"
                                                    "Введите '/train', чтоы начать тренировку"
                                                    "Введите '/profile' чтобы посмотреть статистику")


@bot.message_handler(content_types=['text'])
def weight(message):
    global weight_us, line
    if (message.text + "**" + str(message.from_user.id)) in table.table.keys():
        table.data_save_dict["user_name"] = str(message.text) + "**" + str(message.from_user.id)
        table.data_save_dict["k_train"] = table.table[table.data_save_dict["user_name"]][6]
        while not table.table[table.data_save_dict["user_name"]][line] == "#":
            line += 1
        filling_method(message)
    else:
        table.data_save_dict["user_name"] = str(message.text) + "**" + str(message.from_user.id)
        table.data_save_dict["date"] = time.ctime().split()[1:-1]
        table.data_save_dict
        push_up(message)


@bot.message_handler(content_types=['text'])
def push_up(message):
    global push_up_use
    table.data_save_dict["weight_us"] = message.text
    if not try_int(table.data_save_dict["weight_us"]):
        bot.send_message(message.from_user.id, "Введите свой вес ")
        bot.register_next_step_handler(message, push_up)
    else:
        bot.send_message(message.from_user.id, "Введите максимальное количество отжиманий выполняемых за раз")
        table.data_save_dict["push_up_use"] = message.text
        bot.register_next_step_handler(message, squats)


@bot.message_handler(content_types=['text'])
def squats(message):
    global squats_us
    table.data_save_dict["push_up_use"] = message.text
    if not try_int(table.data_save_dict["push_up_use"]):
        bot.send_message(message.from_user.id, "Введите максимальное количество отжиманий выполняемых за раз ")
        bot.register_next_step_handler(message, squats)
    else:
        bot.send_message(message.from_user.id, "Введите максимальное количество приседаний выполняемых за раз")
        table.data_save_dict["squats_us"] = message.text
        bot.register_next_step_handler(message, plank)


@bot.message_handler(content_types=['text'])
def plank(message):
    global plank_us
    table.data_save_dict["squats_us"] = message.text
    if not try_int(table.data_save_dict["squats_us"]):
        bot.send_message(message.from_user.id, "Введите максимальное количество приседаний выполняемых за раз")
        bot.register_next_step_handler(message, plank)
    else:
        bot.send_message(message.from_user.id, "Введите максимальное время в планке ")
        table.data_save_dict["plank_us"] = message.text
        bot.register_next_step_handler(message, twisting)


@bot.message_handler(content_types=['text'])
def twisting(message):
    global twisting_us
    table.data_save_dict["plank_us"] = message.text
    if not table.data_save_dict["plank_us"]:
        bot.send_message(message.from_user.id, "Введите максимальное время в планке ")
        bot.register_next_step_handler(message, twisting)
    else:
        bot.send_message(message.from_user.id, "Введите максимальное количество скручивания ")
        twisting_us = message.text
        table.data_save_dict["k_train"] = 1 + 1/((int(table.data_save_dict["push_up_use"]) +
                                                  int(table.data_save_dict["squats_us"])
                                                 + int(table.data_save_dict["plank_us"]))/40)
        table.new_user_add(table.data_save_dict)
        table.save()
        table.__init__("Table.xlsx")
        bot.register_next_step_handler(message, filling_method)


@bot.message_handler(content_types=['text'])
def filling_method(message):
    keyboard = types.InlineKeyboardMarkup()

    key_profit = types.InlineKeyboardButton(text="Мышечный набор", callback_data="expenses_hard")
    keyboard.add(key_profit)

    key_profit = types.InlineKeyboardButton(text="Похудение", callback_data="expenses_low")
    keyboard.add(key_profit)

    bot.send_message(message.from_user.id, text="Выберите желаемый челлендж", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def chse_Exercises(message):
    keyboard = types.InlineKeyboardMarkup()
    for train_step in trai_dict()[0][trai_dict()[1]][0]:
        key_profit = types.InlineKeyboardButton(text=train_step, callback_data="train_step")
        keyboard.add(key_profit)

    key_profit = types.InlineKeyboardButton(text="Закончить тренировку ", callback_data="train_end")

    bot.send_message(message.from_user.id, text=("Каждое упрожнения выполнять " +
                                                 str(30 * table.data_save_dict["k_train"])), reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def hard_Exercises(message):
    keyboard = types.InlineKeyboardMarkup()

    key_profit = types.InlineKeyboardButton(text="отжимания", callback_data="expenses_отжим")
    keyboard.add(key_profit)

    key_profit = types.InlineKeyboardButton(text="приседаний", callback_data="expenses_присед")
    keyboard.add(key_profit)

    key_profit = types.InlineKeyboardButton(text="планка", callback_data="expenses_пл")
    keyboard.add(key_profit)

    key_profit = types.InlineKeyboardButton(text="скручивания", callback_data="expenses_ск")
    keyboard.add(key_profit)

    bot.send_message(message.from_user.id, text="Выберите Упражнение", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def like(message):
    keyboard = types.InlineKeyboardMarkup()
    for i in range(1, 11):
        key_profit = types.InlineKeyboardButton(text=i, callback_data="like_i")
        keyboard.add(key_profit)

    bot.send_message(message.from_user.id, text="оцените сложность тренировок ", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "expenses_hard":
        bot.send_message(call.message.chat.id, 'вы выбрали силовой марафон из ежедневных силовых тренировокё\
        в течении 30 дней,каждый день вам будет приходить план тренировок')
        table.data_save_dict["train_type"] = "hard"
        hard_Exercises(call)

    if call.data == "expenses_low":
        bot.send_message(call.message.chat.id, 'вы выбрали кардио марафон направленый на интенсивное похудение.\
        В течении последующих 30 дней вам будет приходить план тренировок')
        table.data_save_dict["train_type"] = "low"
        chse_Exercises(call)

    if "like" in call.data:
        if int(call.data.split("_")[1]) > 5:
            table.data_save_dict["k_train"] += call.data.split("_")[1]/40
        else:
            table.data_save_dict["k_train"] -= 1 - call.data.split("_")[1]/60

    if call.data in weekdays_slimming[t][0]:
        bot.send_photo(weekdays_slimming[t][1][weekdays_slimming[t][0].index(call.data)])
        like(call)


    if call.data == "expenses_отжим":
        bot.send_message(call.message.chat.id, f'сделайте '
                                                    f'отжиманий - {table.table[table.data_save_dict["user_name"]][2] * table.data_save_dict["k_train"]}')
        like(call)

    if call.data == "expenses_присед":
        bot.send_message(call.message.chat.id, f'сделайте '
                                                    f'приседаний - {table.table[table.data_save_dict["user_name"]][3] * table.data_save_dict["k_train"]}')
        like(call)

    if call.data == "expenses_пл":
        bot.send_message(call.message.chat.id, f'стойте в планке '
                                                    f'- {table.table[table.data_save_dict["user_name"]][4] * table.data_save_dict["k_train"]} секунд')
        like(call)

    if call.data == "expenses_ск":
        bot.send_message(call.message.chat.id, f'сделайте скручиваний '
                                                    f'- {table.table[table.data_save_dict["user_name"]][5] * table.data_save_dict["k_train"]}')
        like(call)


bot.polling(none_stop=True, interval=0)
