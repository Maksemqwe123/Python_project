from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cities = ['Гомель', 'Минск', 'Брест', 'Витебск', 'Могилёв', 'Гродно']

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    KeyboardButton(cities[0]),
    KeyboardButton(cities[1]),
    KeyboardButton(cities[2])
).row(
    KeyboardButton(cities[3]),
    KeyboardButton(cities[4]),
    KeyboardButton(cities[5])
)

house_or_street = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    KeyboardButton('Что можно поделать дома ?')
).row(
    KeyboardButton('Как можно провести время на улице ?')
)

help_assistant_house = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Что за акция на пиццу?'),
    KeyboardButton('Какой фильм можно посмотреть?')
).row(
    KeyboardButton('Какую книгу можно почитать?')
).row(
    KeyboardButton('Какой десерт можно легко приготовить?')
)

help_assistant_street = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('На какой фильм в кинотеатр можно сходить ?')
).row(
    KeyboardButton('Куда можно сходить поесть ?')
).row(
    KeyboardButton('Где и какой кофе можно выпить?')
).row(
    KeyboardButton('Какое представление можно посмотреть?')
)
