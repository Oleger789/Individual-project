# Подключаем необходимые файлы и библиотеки для работы
import os
from process_data import get_analytics
from data_service import get_price, show_price, get_product, show_product


MAIN_MENU = \
"""
~~~~~~~~~~~  Обробка зміни рівня ринкових цін ~~~~~~~~~~~

1 - Вивід аналізу зміни рівня ринкових цін
2 - Запис аналізу зміни рівня ринкових цін в файл
3 - Вивід ринкові ціни
4 - вивід довідник товарів
0 - завершення роботи
---------------------------------------------------------
"""

TITLE = "АНАЛІЗ ЗМІНИ РІВНЯ РИНКОВИХ ЦІН"

HEADER = \
"""
===================================================================================================================
|  Найменування товару  |    Рік    |   Середня ринкова ціна за місяць   |   Роздрібна ціна, крб  |  Рівень змін  |
===================================================================================================================
"""

FOOTER = \
'''
===================================================================================================================
'''

STOP_MESSAGE = '\nДля продовження натисніть <Enter>'

# Выводим аналитику
def showAnalytics():
    # Получаем массив с аналитикой
    analytics = get_analytics()

    # Выводим название и шапку
    print(TITLE)
    print(HEADER)

    # Выводим информацию с массива
    for analytic in analytics:
        print(
        f"{analytic['name']:21}",
        f"{analytic['year']:>11}",
        f"{analytic['mid_price']:>36}",
        f"{analytic['retail']:>25}",
        f"{analytic['changes']:>15}"

        )
    # Выводим футер
    print(FOOTER)

# Сохраняем файл с аналитикой
def saveAnalytics(analytics):

    # Открываем файл для записи
    with open("./data/Analytics.txt", "w") as file:
        # В цикле преобразуем к нужному формату и записываем данные в файл
        for analytic in analytics:
            line = \
            analytic['name']   + ';' + \
            str(analytic['year'])    + ';' + \
            str(analytic['mid_price'])  + ';' + \
            str(analytic['retail'])   + ';' + \
            str(analytic['changes'])   + '\n'

            file.write(line)

        print("Сохранение прошло успешно. Путь <./data/Analytics.txt>")

# Запускаем бесконечный цикл для отслеживания коменд от пользователя
while True:

    # Чистим консоль
    os.system("cls")
    # Выводим меню
    print(MAIN_MENU)
    # Даем пользователю выбрать команду
    command = input("Введіть номер команди: ")

    # Обработка команд
    if command == "0":
        os.system("cls")
        print("\nПрограма завершила роботу.")
        exit(0)
    elif command == "1":
        os.system("cls")
        showAnalytics()
        input('\n' + STOP_MESSAGE)
    elif command == "2":
        os.system("cls")
        analytics = get_analytics()
        saveAnalytics(analytics)
        input(STOP_MESSAGE)
    elif command == "3":
        os.system("cls")
        show_price(get_price())
        input(STOP_MESSAGE)
    elif command == "4":
        os.system("cls")
        show_product(get_product())
        input(STOP_MESSAGE)
    else:
        os.system("cls")
        input("\nНекоректний номер команди, для продовження натисніть <Enter>")
