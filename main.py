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
    with open("some.csv", "a") as csv_fh:
        writer = csv.writer(csv_fh, delimiter=':', quoting=csv.QUOTE_MINIMAL, quotechar='`', lineterminator='|')
        writer.writerows([
                          data
                        ])


# def save_info():
#     output_file = open("result.csv", "w")
#     wrtr = csv.DictWriter(output_file, fieldnames=['name', 'number', 'text'])
#     fieldname = dict(name='name', number="number", text='text')
#     rec = dict(name='1', number='2', text='3')
#     wrtr.writerow(fieldname)
#     wrtr.writerow(rec)
#     output_file.close()


def main():
    # выводим высе найденые товары
    print("Start working")
    grab = Grab()
    grab.go(settings.SEARCH_URL.format(settings.PHRASES[0]))
    for i in range(2, 400):
        print("Page:", i)
        items = grab.doc.tree.xpath(settings.XPATH['items'])
        for j, item in enumerate(items):
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
            try:
                seller_link = g.doc.tree.xpath(".//*[@id='merchant-info']/a")[0].get('href')
            except IndexError:
                continue

            seller_id = re.findall(settings.PATTERNS['seller_id'],
                                   seller_link)[0]
            # переходим на страницу с подробными данными по селлеру
            seller_link = settings.SELLER_URL.format(seller_id)
            try:
                g.go(seller_link)
            except GrabTimeoutError as e:
                print("При загрузке", seller_link, "возбуждено исключение", e)
                continue

            try:
                seller_full_info = g.doc.tree.xpath(".//*[@id='aag_detailsAbout']")[0]
            except IndexError:
                print(link)
                print("Seler info not found", settings.SELLER_URL.format(seller_id))
                continue

            seller_full_info_html = tostring(seller_full_info, encoding='utf-8').decode('utf-8')
            seller_full_info = re.sub(r'\<[^>]*\>', '', seller_full_info_html)
            seller_full_info = re.sub(r'(?<=\s)\s', '', seller_full_info)
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
                seller_full_info,]

            save_info(seller_info)

            # with open(seller_info[0] + '.txt', 'w') as f:
            #     f.write(link + '\n')
            #     f.write(seller_link + '\n')
            #     f.write(seller_full_info)
            #     f.write(str(seller_info))
            del g

        next_link = 'https://www.amazon.de'
        next_link += grab.doc.tree.xpath(".//*[@id='pagnNextLink']")[0].get('href')
        grab.go(
            next_link
        )

    del grab


if __name__ in "__main__":
    # save_info()
    main()
