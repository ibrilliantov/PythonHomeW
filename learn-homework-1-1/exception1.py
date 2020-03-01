"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
 1
"""

def ask_user():
    dictt = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}

    while True:
        try:
            user_ask = input('Задайте вопрос: ')
            a = dictt.get(user_ask, "")
            print(a)
        except(KeyboardInterrupt):
            print("\nПока")
            break


if __name__ == "__main__":
    ask_user()
