import configparser
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin_id: int


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config['bot']

    return Config(
        tg_bot=TgBot(
            token=tg_bot['token'],
            admin_id=int(tg_bot['admin_id'])
        )
    )


if __name__ == '__main__':
    config_ = load_config(r'Z:\Troshkin Artem\Pt9\Maxim Markovtsov\food_bot\config\bot_config.ini')
    print(config_)
    print(config_.tg_bot.token)
    print(config_.tg_bot.admin_id)

# class User:
#     def __init__(self, username: str, age: int):
#         self.username = username
#         self.age = age
#
#     def __str__(self):
#         return f'{self.username}, {self.age}'
#
#
# # user = User('Maxim', 16)
# # print(user)
#
# @dataclass
# class SuperUser:
#     username: str
#     age: int
#
#
# user = SuperUser('Maxim', 16)
# print(user.username)
