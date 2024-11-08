import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import time

participants = ["Илья", "Жека", "Кирилл"]
dick_size = list(range(-20, 21))

user_last_command_time_dolboeb = {}
user_last_command_time_size = {}

kirill, ilia, evgen = 0, 0, 0

def start_command(update: Update) -> None:
    keyboard = [['/who_dolboeb']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("Выберите команду:", reply_markup=reply_markup)

def who_command(update: Update) -> None:
    user_id = update.message.from_user.id
    current_time = time.time()

    last_time = user_last_command_time_dolboeb.get(user_id, 0)

    timer = int(30 - (current_time - last_time))

    if current_time - last_time < 30:
        update.message.reply_text(f"че ты жмешь? долбоеб, блять! подожди {timer} секунд...")
        return
    else:
        selected_person = random.choice(participants)
        update.message.reply_text(f"{selected_person} - долбоеб")
    user_last_command_time_dolboeb[user_id] = current_time

def about_me(update: Update) -> None:
    update.message.reply_text("ээээ, бля короче тыкай /who_dolboeb и все, иди нахуй")

def come_back_size_dick(update: Update) -> None:

    user_id = update.message.from_user.id
    current_time = time.time()

    last_time = user_last_command_time_size.get(user_id, 0)
    timer = int(30 - (current_time - last_time))

    if current_time - last_time < 30:
        update.message.reply_text(f"куда ты нахуй хуй растишь?? подожди {timer} секунд...")
        return
    else:
        global ilia, evgen, kirill

        selected_person_size = random.choice(participants)

        if selected_person_size == "Илья":

            random_size = random.choice(dick_size)
            ilia += random_size

            update.message.reply_text(f"Хуй Ильи получает {random_size} см, итого... всего то {ilia} см")

        elif selected_person_size == "Жека":

            random_size = random.choice(dick_size)
            evgen += random_size

            update.message.reply_text(f"Хуй Жеки получает {random_size} см, итого... всего то {evgen} см")

        elif selected_person_size == "Кирилл":

            random_size = random.choice(dick_size)
            kirill += random_size

            update.message.reply_text(f"Хуй Кирилла получает {random_size} см, итого... всего то {kirill} см")

    user_last_command_time_size[user_id] = current_time

def main():
    TOKEN = "8142957369:AAFkQmgERdi0C3R12IHGxKLwsTBQ-JBMsrU"
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("who_dolboeb", who_command))
    dp.add_handler(CommandHandler("come_back_size_dick", come_back_size_dick))
    dp.add_handler(CommandHandler("about_me", about_me))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
