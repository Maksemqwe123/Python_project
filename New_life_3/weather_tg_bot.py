from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot('5943153454:AAG5fynEBoLObp7za7MpfLpVbI8j-ObMORs')
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handler import dp
    executor.start_polling(dp, skip_updates=True)
