#!/usr/bin/python3
# -*- coding: utf-8 -*-
from os import sys
from grab import Grab
import settings

__author__ = 'whoami'
__version__ = '0.0.0'
__date__ = '03.02.16 18:43'
__description__ = """
Парсим amazon. Получаем информацию о продавцах и пишем ее в csv файл.
"""


def main(*args):
    # выводим высе найденые товары
    print(args)
    print("Start working")
    grab = Grab()
    grab.go(settings.SEARCH_URL.format(settings.PHRASES[0]))
    items = grab.doc.tree.xpath(settings.XPATH['items'])
    for item in items:
        link = item.get('href')
        # if`ом исключаем мусор. иногда попадается 3 лишних результата
        if 'keywords=' in link:
            print(link)
            print('\n')
    del grab


if __name__ in "__main__":
    main(sys.argv)
