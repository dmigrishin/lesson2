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

"""
import logging
import config
import ephem
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

planets_set = {"Меркурий":"Mercury", "Венера":"Venus", "Земля":"Earth", "Марс":"Mars", "Юпитер":"Jupiter", "Сатурн":"Saturn", "Уран":"Uranus", "Нептун":"Neptune", "Плутон":"Pluto"}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 
def planet_informer(bot, update):
    now_time = datetime.datetime.now()
    ephem_date = now_time.strftime("%Y/%m/%d")
    user_text = update.message.text
    print('Planet Informer')
    planet_search = user_text.split(' ')
    print (planet_search)
    plnts = "ephem."
    
    
    for planet in planet_search:
        for k,v in planets_set.items():
            if planet in k:
                
                print ("Поиск данных по небесному телу: ", planet)
                plnt = getattr(ephem, v.capitalize())(ephem_date)
                data = ephem.constellation(plnt)
                print (data)
                reply = "Планета в созвездии: " +data[1]
    update.message.reply_text(reply)

def main():
    mybot = Updater(config.SECRET_KEY, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_informer))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
