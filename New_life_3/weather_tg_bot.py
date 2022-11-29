from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from New_life_3.weatear import ru
from config import open_weather_token
from buttons import user_kb, user_kb_1, user_kb_2
from parser_pizza import ref
from parser_kinogo import data, kinogo_data
from parser_litres import datas, litres_data
from cook_parser import data_1, cook_data_1
import requests
import aiofiles
import datetime
import os


bot = Bot('5943153454:AAG5fynEBoLObp7za7MpfLpVbI8j-ObMORs')
dp = Dispatcher(bot)

users = dict()


@dp.message_handler(commands='start')
async def start_Message(message: types.Message):

    if str(message.from_user.id) not in users.keys():
        users[str(message.from_user.id)] = message.from_user.full_name

        async with aiofiles.open('users_data.txt', 'w+') as users_file:
            for ID, username in users.items():
                await users_file.write(f'ID: {ID} | Username: {username}')

    await message.answer('Привет, я бот который подскажет как провести день, в связи с погодой', reply_markup=user_kb)
    await message.answer('В каком городе ты хочешь узнать погоду?')


@dp.message_handler(Text(equals='Гомель', ignore_case=True))
async def today(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang={ru}"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        await message.answer(f'В городе: {city} \nТемпература воздуха: {cur_weather} C \nОжидается: {weather_description}\n'
                             f'Скорость ветра: {wind} м/c', reply_markup=user_kb_1)

        if cur_weather < 5 and cur_weather > -4:
            await message.answer('сегодня ожидается слякоть, оденьте обувь на высокой подошве или останься дома и ...')

        elif cur_weather >= -5 and cur_weather <= -8:
            await message.answer('сейчас на улице холодно, оденься потеплее, желательно ещё поесть перед выходом')

        elif cur_weather > -9 and cur_weather < -16:
            await message.answer('сейчас на улице довольно холодно, посоветую тебе остаться дома,'
                                 ' но если тебе не страшен холод, могу посоветовать куда можно сходить  ')

        elif cur_weather > -16:
            await message.answer('cейчас на улице очень холодно, останься лучше дома')


    except:
        await message.reply("Проверьте название города")


@dp.message_handler(Text(equals='Минск', ignore_case=True))
async def today(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang={ru}"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        await message.answer(f'В городе: {city} \nТемпература воздуха: {cur_weather} C \nОжидается: {weather_description}\n'
                             f'Скорость ветра: {wind} м/c', reply_markup=user_kb_1)

        if cur_weather < 5 and cur_weather > -4:
            await message.answer('сегодня ожидается слякоть, оденьте обувь на высокой подошве или останься дома и ...')

        elif cur_weather >= -5 and cur_weather <= -8:
            await message.answer('сейчас на улице холодно, оденься потеплее, желательно ещё поесть перед выходом')

        elif cur_weather > -9 and cur_weather < -16:
            await message.answer('сейчас на улице довольно холодно, посоветую тебе остаться дома,'
                                 ' но если тебе не страшен холод, могу посоветовать куда можно сходить  ')

        elif cur_weather > -16:
            await message.answer('cейчас на улице очень холодно, останься лучше дома')


    except:
        await message.reply("Проверьте название города")


@dp.message_handler(Text(equals='Брест', ignore_case=True))
async def today(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang={ru}"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        await message.answer(f'В городе: {city} \nТемпература воздуха: {cur_weather} C \nОжидается: {weather_description}\n'
                             f'Скорость ветра: {wind} м/c', reply_markup=user_kb_1)

        if cur_weather < 5 and cur_weather > -4:
            await message.answer('сегодня ожидается слякоть, оденьте обувь на высокой подошве или останься дома и ...')

        elif cur_weather >= -5 and cur_weather <= -8:
            await message.answer('сейчас на улице холодно, оденься потеплее, желательно ещё поесть перед выходом')

        elif cur_weather > -9 and cur_weather < -16:
            await message.answer('сейчас на улице довольно холодно, посоветую тебе остаться дома,'
                                 ' но если тебе не страшен холод, могу посоветовать куда можно сходить  ')

        elif cur_weather > -16:
            await message.answer('cейчас на улице очень холодно, останься лучше дома')


    except:
        await message.reply("Проверьте название города")


@dp.message_handler(Text(equals='Витебск', ignore_case=True))
async def today(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang={ru}"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        await message.answer(f'В городе: {city} \nТемпература воздуха: {cur_weather} C \nОжидается: {weather_description}\n'
                             f'Скорость ветра: {wind} м/c', reply_markup=user_kb_1)

        if cur_weather < 5 and cur_weather > -4:
            await message.answer('сегодня ожидается слякоть, оденьте обувь на высокой подошве или останься дома и ...')

        elif cur_weather >= -5 and cur_weather <= -8:
            await message.answer('сейчас на улице холодно, оденься потеплее, желательно ещё поесть перед выходом')

        elif cur_weather > -9 and cur_weather < -16:
            await message.answer('сейчас на улице довольно холодно, посоветую тебе остаться дома,'
                                 ' но если тебе не страшен холод, могу посоветовать куда можно сходить  ')

        elif cur_weather > -16:
            await message.answer('cейчас на улице очень холодно, останься лучше дома')


    except:
        await message.reply("Проверьте название города")


@dp.message_handler(Text(equals='Могилёв', ignore_case=True))
async def today(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang={ru}"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        await message.answer(f'В городе: {city} \nТемпература воздуха: {cur_weather} C \nОжидается: {weather_description}\n'
                             f'Скорость ветра: {wind} м/c', reply_markup=user_kb_1)

        if cur_weather < 5 and cur_weather > -4:
            await message.answer('сегодня ожидается слякоть, оденьте обувь на высокой подошве или останься дома и ...')

        elif cur_weather >= -5 and cur_weather <= -8:
            await message.answer('сейчас на улице холодно, оденься потеплее, желательно ещё поесть перед выходом')

        elif cur_weather > -9 and cur_weather < -16:
            await message.answer('сейчас на улице довольно холодно, посоветую тебе остаться дома,'
                                 ' но если тебе не страшен холод, могу посоветовать куда можно сходить  ')

        elif cur_weather > -16:
            await message.answer('cейчас на улице очень холодно, останься лучше дома')


    except:
        await message.reply("Проверьте название города")


@dp.message_handler(Text(equals='Гродно', ignore_case=True))
async def today(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang={ru}"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        await message.answer(f'В городе: {city} \nТемпература воздуха: {cur_weather} C \nОжидается: {weather_description}\n'
                             f'Скорость ветра: {wind} м/c', reply_markup=user_kb_1)

        if cur_weather < 5 and cur_weather > -4:
            await message.answer('сегодня ожидается слякоть, оденьте обувь на высокой подошве или останься дома и ...')

        elif cur_weather >= -5 and cur_weather <= -8:
            await message.answer('сейчас на улице холодно, оденься потеплее, желательно ещё поесть перед выходом')

        elif cur_weather > -9 and cur_weather < -16:
            await message.answer('сейчас на улице довольно холодно, посоветую тебе остаться дома,'
                                 ' но если тебе не страшен холод, могу посоветовать куда можно сходить  ')

        elif cur_weather > -16:
            await message.answer('cейчас на улице очень холодно, останься лучше дома')


    except:
        await message.reply("Проверьте название города")


@dp.message_handler(Text(equals='Что можно поделать дома ?', ignore_case=True))
async def leisure(message: types.Message):
    await message.answer('можно посмотреть/почитать фильм/книгу, но перед этим, я бы посоветовал заварить чая/кофе.\n'
                         'могу подсказать как легко и просто приготовить вкусный десерт,'
                         'так же проходит акция при заказе пиццы', reply_markup=user_kb_2)


@dp.message_handler(Text(equals='Что за акция на пиццу?', ignore_case=True))
async def pizza(message: types.Message):
    await message.answer(f'{ref}')


@dp.message_handler(Text(equals='Какой фильм можно посмотреть?', ignore_case=True))
async def kinogo(message: types.Message):
    await message.answer(f'Название: {kinogo_data[1]} \n{data[1]}\n')
    await message.answer(f'Название: {kinogo_data[2]} \n{data[2]}\n')
    await message.answer(f'Название: {kinogo_data[3]} \n{data[3]}\n')
    await message.answer(f'Название: {kinogo_data[4]} \n{data[4]}\n')


@dp.message_handler(Text(equals='Какую книгу можно почитать?', ignore_case=True))
async def book(message: types.Message):
    await message.answer(f'Название:{litres_data[1]} \n{datas[1]}\n')
    await message.answer(f'Название:{litres_data[2]} \n{datas[2]}\n')
    await message.answer(f'Название:{litres_data[3]} \n{datas[3]}\n')
    await message.answer(f'Название:{litres_data[4]} \n{datas[4]}\n')


@dp.message_handler(Text(equals='Какой десерт можно легко приготовить?', ignore_case=True))
async def cook(message: types.Message):
    await message.answer(f'Название: {cook_data_1[1]} \n{data_1[1]}\n')
    await message.answer(f'Название: {cook_data_1[2]} \n{data_1[2]}\n')
    await message.answer(f'Название: {cook_data_1[3]} \n{data_1[3]}\n')
    await message.answer(f'Название: {cook_data_1[4]} \n{data_1[4]}\n')

# @dp.callback_query_handlers(func=lambda call: True)
# async def check(callback: types.CallbackQuery):
#     if callback.data == 'Гомель':
#         return await

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
