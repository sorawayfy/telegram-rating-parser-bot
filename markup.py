from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from config import UNIVERSITIES

data_cb = CallbackData('data', 'action', 'name')  # CALLBACK FOR UN


# btnMain = KeyboardButton('Главное меню')

# Main Menu
btnSelectUniversity = KeyboardButton('Выбрать вуз')
btnOther = KeyboardButton('Другое')

navMainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    btnSelectUniversity, btnOther)

# University select TODO: (by city)

# universityMenu = ReplyKeyboardMarkup()


mainMenu = InlineKeyboardMarkup(row_width=6)

for university in UNIVERSITIES:
    print('INSERTED')
    mainMenu.insert(InlineKeyboardButton(
        text=university["name"], callback_data=data_cb.new(action="click", name=university["callback"])))
