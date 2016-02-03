#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
from os import sys
from lxml.html import tostring
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

            # переходим по линке на итем
            g = Grab()
            g.go(link)
            try:
                seller_link = g.doc.tree.xpath(".//*[@id='merchant-info']/a")[0].get('href')
            except IndexError:
                print("Item", link, ": Seller not found.")
                continue

            seller_id = re.findall(settings.PATTERN, seller_link)[0]
            # переходим на страницу с подробными данными по селлеру
            g.go(settings.SELLER_URL.format(seller_id))

            # seller_info = g.doc.tree.xpath(".//*[@id='aag_detailsAbout']")[0]
            # print(tostring(seller_info, encoding='utf-8'))

            name = ".//*[@id='aag_detailsAbout']/h3"
            register_name = ".//*[@id='aag_detailsAbout']/p/strong/span[2]"
            adress = ".//*[@id='aag_detailsAbout']/p/strong/span[3]"
            telephone = ".//*[@id='aag_detailsAbout']/p/strong/span[4]"
            telephaks = ".//*[@id='aag_detailsAbout']/p/strong/span[5]"
            email = ".//*[@id='aag_detailsAbout']/p/strong/span[7]"
            register_data = ".//*[@id='aag_detailsAbout']/p/strong/span[9]"

            xpaths = [name, register_name, adress, telephone, telephaks, email, register_data]

            for xpath in xpaths:
                data = g.tree.xpath(xpath)[0].text
                print(data)
            # емайл закодили совсем по тупому... но это решаемо
            email = g.tree.xpath(xpaths[5])[0]
            print(tostring(email, encoding='utf-8'))

    del grab


if __name__ in "__main__":
    main(sys.argv)
