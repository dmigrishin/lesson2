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

planets_set = {
    "Меркурий":"Mercury",
    "Венера":"Venus",
    "Земля":"Earth",
    "Марс":"Mars",
    "Юпитер":"Jupiter",
    "Сатурн":"Saturn",
    "Уран":"Uranus",
    "Нептун":"Neptune",
    "Плутон":"Pluto"
    }

constellations_set = {
"Aquarius":"Водолей",
"Aries" :"Овен",
"Cancer":"Рак",
"Capricornus":"Козерог",
"Gemini":"Близнецы",
"Leo":"Лев",
"Libra":"Весы",
"Pisces":"Рыбы",
"Sagittarius":"Стрелец",
"Scorpius":"Скорпион",
"Taurus":"Телец",
"Virgo":"Дева"
}

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
    print('Запуск скрипта Planet Informer')
    now_time = datetime.datetime.now()
    ephem_date = now_time.strftime("%Y/%m/%d")
    user_text = update.message.text
    planet_search = user_text.split(' ')
    planet_search.remove('/planet')
        
    if (planet_search[0] in planets_set) and (len(planet_search) !=0):
        print ("Поиск данных по небесному телу: ", planet_search[0])
        planet = getattr(ephem, planets_set.get(planet_search[0]).capitalize())(ephem_date)
        data = ephem.constellation(planet)
        print (data)
        reply = '{} Планета {} находится в созвездии {}'.format(ephem_date,
        planet_search[0], constellations_set.get(str(data[1])))
        print (reply)
    else:
        print('Нет такой планеты')
        reply = "Нет такой планеты"

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
