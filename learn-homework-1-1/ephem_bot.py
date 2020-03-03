"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.
1
"""
import logging
import ephem
from PythonHomeW.lesson1 import settings
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

def planet_command(bot, update):
    now = datetime.datetime.now()
    user_text = update.message.text
    p = user_text.split()
    wat = getattr(ephem, p[1])(now)
    const = ephem.constellation(wat)
    print(const)
    update.message.reply_text(const)


def greet_user(bot, update):
    text = 'Напиши например: /planet Mars и узнаешь в каком созвездии эта планета сейчас. ' \
           'Или другие планеты: Mercury, Venus, Jupiter, Saturn, Uranus, Neptune'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(settings.BOT_TOKEN, request_kwargs=settings.PROXY, use_context=False)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_command))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()



# Mercury	 Меркурий
#  Venus	 Венера
#  Earth	 Земля
#  Mars	 Марс
#  Jupiter	 Юпитер
#  Saturn	 Сатурн
#  Uranus	 Уран
#  Neptune	 Нептун
#  Pluto	 Плутон