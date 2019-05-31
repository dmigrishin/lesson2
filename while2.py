"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
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
    # print(small_talking.get(user_response))

    condition = True
    while condition is not None:
        user_response = input('Ну скажи что-нибудь: ')
        condition = small_talking.get(user_response)
        bot_response = small_talking.get(user_response) if small_talking.get(user_response) is not None else "Чао какао!"
        print(bot_response)
        
if __name__ == "__main__":
    ask_user()
