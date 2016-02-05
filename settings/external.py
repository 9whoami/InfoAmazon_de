# -*- coding: utf-8 -*-

# Ссылка на страницу с подробным описанием продавца. Вместо {} будет подставлен id продавца
SELLER_URL = "http://www.amazon.de/gp/aag/details/ref=aag_m_as?ie=UTF8&asin=&isAmazonFulfilled=&isCBA=&seller={}"

#
XPATH = dict(
    items='.//*/a[@class="a-link-normal s-access-detail-page  a-text-normal"]',
    next_page=".//*[@id='pagnNextLink']",
    seller_info=".//*[@id='aag_detailsAbout']",
    seller_link=".//*[@id='merchant-info']/a"

)

# Паттерны регулярных выражений
PATTERNS = dict(
    # Поиск id селлера из урл
    seller_id=r'&seller\=(.+)',
    # Получение имени продавца
    name=r'\<h3\>(.+?)\s\<\/h3\>',
    # Телефон
    phone=r'[Telefon|Tel|Phone]:\s*([0-9\-\s\(\)\/\+]+)\<',
    # Факс
    fax=r'[Telefax|Fax]:\s([0-9\-\s\(\)\/\+]+)\<',
    # Сайт
    site=r'www\.(.+?)\<',
    # Мыло
    email=r'[Email|E-Mail|eMail]:.+?([A-z0-9\_\-\.]+@[A-z0-9\.\-]+\.[A-z0-9]+)\<'
)
