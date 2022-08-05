from config import TOKEN, FUNCTIONS, UNIVERSITIES
from markup import data_cb
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
    university = State()


@dp.message_handler(commands=['start'])
async def greeting(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, я помогу тебе найти свое место в рейтинговых списках', reply_markup=nav.navMainMenu)


@dp.message_handler()
async def send_message(message: types.Message):
    if message.text == 'Выбрать вуз':
        await Form.snils.set()

        await bot.send_message(message.from_user.id, 'Введи свой СНИЛС:')


@dp.message_handler(state=Form.snils)
async def process_name(message: types.Message, state: FSMContext):
    if message.text.isdigit() and len(message.text) == 11:
        async with state.proxy() as data:
            data['snils'] = message.text

        # await bot.send_message(message.from_user.id, 'Выберите ВУЗ', reply_markup=nav.mainMenu)
        await Form.university.set()
        await bot.send_message(message.from_user.id, 'Введите аббревиатуру своего вуза:')
    else:
        await Form.snils.set()
        await bot.send_message(message.from_user.id, emoji.emojize('Неверный СНИЛС :thumbs_up:, повторите ввод'))


@dp.message_handler(state=Form.university)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['university'] = message.text
    for un in UNIVERSITIES:
        if un["name"].lower() == message.text.lower():
            await FUNCTIONS[un["callback"]](bot, message.from_user.id)


# @dp.callback_query_handler(data_cb.filter(action='click'))
# async def random(query: types.CallbackQuery, callback_data: dict):
#     print('CLK')
#     data = FUNCTIONS[callback_data["name"]]
#     print(bot, query["from"]["id"])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
