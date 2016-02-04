#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import csv
import logging
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
COUNT_REQUEST = 0


def save_info(data):
    with open(settings.OUT_FILE[0], "a") as csv_fh:
        writer = csv.writer(csv_fh, **settings.CSV)
        writer.writerows([
            data
        ])


def get_search_url():
    if isinstance(settings.SEARCH_URL, tuple):
        for url in settings.SEARCH_URL:
            yield url
    else:
        for phrase in settings.PHRASES:
            yield settings.SEARCH_URL.format(phrase)


def page_load(grab, url):
    global COUNT_REQUEST
    if COUNT_REQUEST > 3:
        raise SystemExit("Load error")
    try:
        document = grab.go(url)
        COUNT_REQUEST = 0
        return document
    except GrabTimeoutError:
        print("Load timeout in url:\n", url, "\nTry change proxy...")
        grab.change_proxy()
        COUNT_REQUEST += 1
        return page_load(grab, url)


def start_grab():
    grab = Grab()
    if settings.USE_PROXY:
        grab.load_proxylist(**settings.PROXY)
    return grab


def get_item_href(items):
    for item in items:
        href = item.get('href')
        if 'keywords=' not in href:
            continue
        yield href


def get_seller_id(grab):
    # получаем ссылку на продавца
    try:
        seller_link = grab.doc.tree.xpath(settings.XPATH['seller_link'])[
            0].get('href')
        return re.findall(settings.PATTERNS['seller_id'], seller_link)[0]
    except IndexError:
        return None


def main():
    # выводим высе найденые товары
    print("Start working")

    grab = start_grab()

    get_nex_url = get_search_url()

    while True:
        try:
            page_load(grab, get_nex_url.__next__())
        except StopIteration:
            raise SystemExit("Working end")

        items = get_item_href(grab.doc.tree.xpath(settings.XPATH['items']))
        for link in items:
            # переходим по линке на итем
            g = start_grab()
            page_load(g, link)

            seller_id = get_seller_id(g)

            if seller_id is None:
                continue

            # переходим на страницу с подробными данными по селлеру
            seller_link = settings.SELLER_URL.format(seller_id)
            page_load(g, seller_link)

            # получаем подробную информацию по селлеру
            try:
                web_element = \
                g.doc.tree.xpath(settings.XPATH['seller_info'])[0]
            except IndexError:
                print("Link to seller info not found",
                      settings.SELLER_URL.format(seller_id))
                continue

            seller_full_info_html = tostring(web_element,
                                             encoding='utf-8').decode('utf-8')
            # очищаем информацию по селлеру от тегов
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
            pass

        page_load(grab, next_link)

    del grab


if __name__ in "__main__":
    main()
