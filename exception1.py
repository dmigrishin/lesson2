"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
small_talking = {
        "Привет":"Ку",
        "Как дела?":"Очень хорошо",
        "Чем занимаешься?":"Отвечаю на вопросы",
        "Можно?":"Нельзя!",
        "Que tal la vida?":"Muy bien!",
        "Hi":"Hello Kitty"
    }

def ask_user():
    """
    Замените pass на ваш код
    """
    print('Я птица говорун! Умею поддерживать разговор на следующие темы: ','\n')
    
    for k in small_talking:
        print(k)
    
    print('\n')
    # user_response = input('Ну скажи что-нибудь: ')
    
    # if small_talking.get(user_response) is None:
    #     print('Краткость сестра таланта!')
    # else:
    #     print(small_talking.get(user_response))
    
    condition = True

    while condition:
        try:
            user_response = input('Ну скажи что-нибудь: ')
            condition = small_talking.get(user_response)
            bot_response = condition if condition is not None else "Чао какао!"
            print(bot_response)
        except KeyboardInterrupt:
            print('пока :(')
            break
    
if __name__ == "__main__":
    ask_user()
