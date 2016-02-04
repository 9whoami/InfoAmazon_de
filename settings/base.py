# -*- coding: utf-8 -*-


class QuoteParam:
    ALL = 1
    MINIMAL = 0
    NONE = 3
    NONNUMERIC = 2

# Урл для поиска товаров. Вместо '{}' будут подставлены поисковые выражения.
SEARCH_URL = "http://www.amazon.de/s/ref=nb_sb_noss?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=node%3D1981733031&field-keywords={}"

# Поисковые выражения
PHRASES = (
    'Bra damen',
)

# Список прокси
PROXY_LIST = (

)

# настройка параметров записи в csv файл
OUT_FILE = 'out.csv',  # имя файла для вывода
CSV = dict(
    delimiter=':',  # разделитель значений
    quoting=QuoteParam.MINIMAL,  # параметр цитирования
    quotechar='`',  # символ цитирования
    lineterminator='|'  # разделитель строк
)
