#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    spisoks = []
    def add():
        # Запрос данных .
        name = input("Фамилия, Имя ")
        tel = input("Номер группы ")
        date = input("оценки (успеваемость) ")

        # Создать список.
        spisok = {
            'name': name,
            'tel': tel,
            'date': date}

        # Добавить елементы в список.
        spisoks.append(spisok)
        # Отсортировать список в случае необходимости.
        if len(spisok) > 1:
            spisoks.sort(key=lambda item: item.get('tel', ''))

    def list():
         # Заголовок таблицы.
         line = '+-{}-+-{}-+-{}-+'.format(
             '-' * 30,
             '-' * 20,
             '-' * 8
         )
         print(line)
         print(
             '| {:^30} | {:^20} | {:^8} |'.format(
                 "Фамилия, Имя",
                 "Номер группы",
                 "оценки (успеваемость) ",
             )
         )
         print(line)

         # Вывести данные .
         for idx, product in enumerate(spisoks, 1):
             print(
                 '| {:<30} | {:<20} | {:>8} |'.format(
                     product.get('name', ''),
                     product.get('tel', ''),
                     product.get('date', 0)
                 )
             )

         print(line)
    def select():
        parts = command.split(' ', maxsplit=2)
        sel = (parts[1])

        count = 0
        for spisok in spisoks:
            if spisok.get('name') == sel:
                count = "оценки (успеваемость) "
                print(
                    '{:>4}: {}'.format(count, spisok.get('date', ''))
                )
                print('Номер группы', spisok.get('tel', ''))
                print('Фамилия Имя', spisok.get('name', ''))

        # Если счетчик равен 0, то люди не найдены.
        if count == 0:
            print("Люди не найден.")

    def help():
        # Вывести список команд.
        print("Список команд:\n")
        print("add - добавить человека;")
        print("list - вывести список людей;")
        print("select <товар> - информация о человеке;")
        print("help - отобразить справку;")
        print("exit - завершить работу с программой.")


    # Список .
    spisoks = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>>>>>",).lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            add()

        elif command == 'list':
            list()

        elif command.startswith('select '):
            select()

        elif command == 'help':
           help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
