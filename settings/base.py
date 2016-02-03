# -*- coding: utf-8 -*-

# Урл для поиска товаров. Вместо '{}' будут подставлены поисковые выражения.
SEARCH_URL = "http://www.amazon.de/s/ref=nb_sb_noss?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=node%3D1981733031&field-keywords={}"

SELLER_URL = "http://www.amazon.de/gp/aag/details/ref=aag_m_as?ie=UTF8&asin=&isAmazonFulfilled=&isCBA=&seller={}"

# Поисковые выражения
PHRASES = (
    'Bra damen',
)

# Список прокси
PROXY_LIST = (

)

XPATH = dict(
    items='.//*/a[@class="a-link-normal s-access-detail-page  a-text-normal"]',

)

PATTERN = '&seller=(.+)'