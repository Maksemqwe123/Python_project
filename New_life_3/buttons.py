from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    KeyboardButton('Гомель'),
    KeyboardButton('Минск'),
    KeyboardButton('Брест')
).row(
    KeyboardButton('Витебск'),
    KeyboardButton('Могилёв'),
    KeyboardButton('Гродно')
)

user_kb_1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    KeyboardButton('что можно поделать дома ?')
)

user_kb_2 = ReplyKeyboardMarkup(resize_keyboard=True).row(
    KeyboardButton('Что за акция на пиццу?'),
    KeyboardButton('Какой фильм можно посмотреть?')
).row(
    KeyboardButton('Какую книгу можно почитать?')
).row(
    KeyboardButton('Какой десерт можно легко приготовить?')
)
# one_time_keyboard=True