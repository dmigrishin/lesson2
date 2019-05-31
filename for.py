"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_scores = [
        {'school_class': '1а', 'scores': [3,5,4,3,2]},
        {'school_class': '1б', 'scores': [4,3,5,3,3]},
        {'school_class': '1в', 'scores': [5,5,3,4,3]}
        ]
    
    list_result=[]
    summ = 0
    count = 0

    for scc in school_scores:
        avgsumm = 0
        avgcount=0
        for k, v in scc.items():
            if "scores" in k:
                for value in v:
                    #print (value)
                    avgsumm += value
                    avgcount+=1
                    summ += value
                    count+= 1
        if avgcount != 0:
            avgresult = avgsumm/avgcount
        
        list_result.append('Средний балл по классу {} :'.format(scc['school_class'],avgresult))

    result = summ/count
    print('Средний балл по школе:', result)
    for l in list_result:
        print(l)

if __name__ == "__main__":
    main()
