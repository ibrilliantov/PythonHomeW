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

#  используй функцию dictt.get(user_ask, "") - вернет значение в словаре по ключу в переменной user_ask, вернет "" если такого ключа нет
def ask_user_dict():
    dictt = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}

    while True:
            user_ask = input('Задайте вопрос: ')
            a = dictt.get(user_ask, "")
            print(a)
            if user_ask == 'Пока':
                print('Ну пока')
                break


if __name__ == "__main__":
    ask_user_dict()
