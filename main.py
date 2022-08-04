from config import TOKEN, FUNCTIONS
from markup import un_data
# import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import markup as nav
import emoji

bot = Bot(token=TOKEN)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    snils = State()


@dp.message_handler(commands=['start'])
async def greeting(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет', reply_markup=nav.navMainMenu)


@dp.message_handler()
async def send_message(message: types.Message):
    if message.text == 'Выбрать вуз':
        await Form.snils.set()

        await bot.send_message(message.from_user.id, 'Введи свой СНИЛС:')


@dp.message_handler(state=Form.snils)
async def process_name(message: types.Message, state: FSMContext):
    """
    Process user name 
    """
    if message.text.isdigit() and len(message.text) == 11:
        async with state.proxy() as data:
            data['snils'] = message.text

        await bot.send_message(message.from_user.id, 'Выберите ВУЗ', reply_markup=nav.mainMenu)
    else:
        await Form.snils.set()
        await bot.send_message(message.from_user.id, emoji.emojize('Неверный СНИЛС :thumbs_up:, повторите ввод'))


@dp.callback_query_handler(un_data.filter(action='Execute'))
async def random(query: types.CallbackQuery, callback_data: dict):
    data = FUNCTIONS[callback_data["name"]]
    await data(bot, query["from"]["id"])

    # await bot.delete_message(message.from_user.id, message.message.message_id)
    # await bot.send_message(message.from_user.id, 'Привет', reply_markup=nav.mainMenu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
