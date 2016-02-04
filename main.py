#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import csv
from lxml.html import tostring
from grab import Grab
from grab.error import GrabTimeoutError
import settings

__author__ = 'whoami'
__version__ = '0.1.0'
__date__ = '03.02.16 18:43'
__description__ = """
Парсим amazon. Получаем информацию о продавцах и пишем ее в csv файл.
"""


def save_info(data):
    with open(settings.OUT_FILE[0], "a") as csv_fh:
        writer = csv.writer(csv_fh, **settings.CSV)
        writer.writerows([
            data
        ])


def main():
    # выводим высе найденые товары
    print("Start working")
    grab = Grab()
    grab.go(settings.SEARCH_URL.format(settings.PHRASES[0]))
    for i in range(1, 400):
        print("Page:", i)
        items = grab.doc.tree.xpath(settings.XPATH['items'])
        for item in items:
            link = item.get('href')
            # if`ом исключаем мусор. иногда попадается 3 лишних результата
            if 'keywords=' not in link:
                continue
            # переходим по линке на итем
            g = Grab()
            try:
                g.go(link)
            except GrabTimeoutError as e:
                print("При загрузке", link, "возбуждено исключение", e)
                continue
            # получаем ссылку на продавца
            try:
                seller_link = g.doc.tree.xpath(settings.XPATH['seller_link'])[
                    0].get('href')
            except IndexError:
                continue
            # из ссылки на продавца получаем ид
            seller_id = re.findall(settings.PATTERNS['seller_id'],
                                   seller_link)[0]
            # переходим на страницу с подробными данными по селлеру
            seller_link = settings.SELLER_URL.format(seller_id)
            try:
                g.go(seller_link)
            except GrabTimeoutError as e:
                print("При загрузке", seller_link, "возбуждено исключение", e)
                continue
            # получаем подробную информацию по селлеру
            try:
                seller_full_info = \
                g.doc.tree.xpath(settings.XPATH['seller_info'])[0]
            except IndexError:
                print(link)
                print("Seler info not found",
                      settings.SELLER_URL.format(seller_id))
                continue
            # очищаем информацию по селлеру от тегов
            seller_full_info_html = tostring(seller_full_info,
                                             encoding='utf-8').decode('utf-8')
            seller_full_info = re.sub(r'\<[^>]*\>', '', seller_full_info_html)
            seller_full_info = re.sub(r'(?<=\s)\s', '', seller_full_info)
            # записываем данные о продавце в список
            seller_info = [
                re.findall(settings.PATTERNS['name'], seller_full_info_html,
                           re.MULTILINE),
                re.findall(settings.PATTERNS['email'], seller_full_info_html,
                           re.MULTILINE),
                re.findall(settings.PATTERNS['phone'], seller_full_info_html,
                           re.MULTILINE),
                re.findall(settings.PATTERNS['fax'], seller_full_info_html,
                           re.MULTILINE),
                re.findall(settings.PATTERNS['site'], seller_full_info_html,
                           re.MULTILINE),
                seller_link,
                seller_full_info]

            save_info(seller_info)

            del g

        # пытаемся получить ссылку на селдующую страницу
        next_link = 'https://www.amazon.de'
        try:
            next_link += grab.doc.tree.xpath(settings.XPATH['next_page'])[
                0].get('href')
        except IndexError:
            raise SystemExit("Working stop. Element 'next page' not found")
        grab.go(next_link)

    del grab


if __name__ in "__main__":
    main()
