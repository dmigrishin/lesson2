"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def check_two_strings(str_one, str_two):
    if type(str_one) is not str or type(str_two) is not str:
        
        return 0 
    if str_one == str_two:
        return 1
    if str_one != str_two and len(str_one)>len(str_two):
        return 2
    if str_one != str_two and str_two == 'learn':
        return 3
    else:
        return 'Функция ничего не делает'
        
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    string_one=str(input('Введите значение первой строки: '))
    string_two=str(input('Введите значение второй строки: '))
    
    choose_result = input ('Хочешь преобразовать первую строку в число? :')
    
    if choose_result == 'Да' or choose_result == 'Yes' or choose_result == 'y':
        try:
            string_one = int(string_one)
        except ValueError:
            print("Первая строка не является числом, попробуй заново")
        
    result_of_check = check_two_strings(string_one,string_two)
    print (result_of_check)

if __name__ == "__main__":
    main()
