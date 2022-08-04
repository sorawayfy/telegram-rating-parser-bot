from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from config import UNIVERSITIES

un_data = CallbackData('data', 'action', 'name')  # CALLBACK FOR UN


# btnMain = KeyboardButton('Главное меню')

# Main Menu
btnSelectUniversity = KeyboardButton('Выбрать вуз')
btnOther = KeyboardButton('Другое')

navMainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    btnSelectUniversity, btnOther)

# University select TODO: (by city)

# universityMenu = ReplyKeyboardMarkup()


mainMenu = InlineKeyboardMarkup(row_width=4)

for university in UNIVERSITIES:
    mainMenu.insert(InlineKeyboardButton(
        text=university["name"], callback_data=un_data.new(name=university["callback"], action="Execute")))
