from background import keep_alive
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import time
from config import TOKEN

user_list = {}
user_last_command_time_dolboeb = {}
user_last_command_time_size = {}

async def start_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name

    if user_id not in user_list:
        user_list[user_id] = {'name': user_name, 'size': 0, 'count_dolboeb': 0}
        await update.message.reply_text(f"{user_name} записан в список долбоёбов, но только пока карандашом...")
    else:
        await update.message.reply_text("ты уже в списке потенциальных долбоёбов!")


async def who_command(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    current_time = time.time()

    last_time = user_last_command_time_dolboeb.get(user_id, 0)
    timer = int(60 - (current_time - last_time))

    if current_time - last_time < 60:
        await update.message.reply_text(f"че ты жмешь? долбоеб, блять! подожди {timer} секунд...")
    else:
        if not user_list:
            await update.message.reply_text("Список пуст.")
            return

        random_user_id = random.choice(list(user_list.keys()))
        user_list[random_user_id]['count_dolboeb'] += 1
        await update.message.reply_text(
            f"{user_list[random_user_id]['name']} - долбоеб, уже {user_list[random_user_id]['count_dolboeb']} раз(а)!")

    user_last_command_time_dolboeb[user_id] = current_time


async def come_back_size_dick(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    current_time = time.time()

    last_time = user_last_command_time_size.get(user_id, 0)
    timer = int(60 - (current_time - last_time))

    if current_time - last_time < 60:
        await update.message.reply_text(f"куда ты нахуй хуй растишь?? подожди {timer} секунд...")
        return
    else:
        if not user_list:
            await update.message.reply_text("никто не записался на увеличения хуя")
            return

        how_change_size = list(range(-20, 21))
        change_dick_size = random.choice(how_change_size)

        user_list[user_id]['size'] += change_dick_size

        await update.message.reply_text(
            f"хуй {user_list[user_id]['name']} получает {change_dick_size} см, итого... всего-то {user_list[user_id]['size']} см")
    user_last_command_time_size[user_id] = current_time

async def list_dolboebov(update: Update, context: CallbackContext) -> None:
    if not user_list:
        await update.message.reply_text("Список пуст.")
        return

    result = ""
    for i, (user_id, user_data) in enumerate(user_list.items(), start=1):
        result += f"{user_data['name']} имеет хуй размером в {user_data['size']} см и был долбоебом {user_data['count_dolboeb']} раз\n"

    await update.message.reply_text(result)

async def about_me(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("ээээ, бля короче тыкай /who_dolboeb, /come_back_size_dick и все, иди нахуй")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("who_dolboeb", who_command))
    application.add_handler(CommandHandler("come_back_size_dick",come_back_size_dick))
    application.add_handler(CommandHandler("list_dolboebov", list_dolboebov))
    application.add_handler(CommandHandler("about_me", about_me))

    keep_alive()
    application.run_polling()

if __name__ == "__main__":
    main()
