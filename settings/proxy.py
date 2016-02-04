# -*- coding: utf-8 -*-


class ProxyType:
    HTTP = 'http'
    SOCKS4 = 'socks4'
    SOCKS5 = 'socks5'


class SourceType:
    URL = 'url'
    FILE = 'text_file'


PROXY = dict(
    # Список прокси. Поддерживается 2 формата:
    # Простой формат "server:port"
    # Сложный формат "server:port:username:password".
    # Используйте сложный формат, если прокси-сервер требует авторизации.
    # В параметре указать путь к файлу либо прямую ссылку на файл
    source='http://dcroid.ru/proxy_list.php',
    # Тип списка, url это или путь к файлу
    source_type=SourceType.URL,
    # Тип прокси
    proxy_type=ProxyType.HTTP,
    # Один раз выбирает случайный прокси-сервер,
    # который используется для всех дальнейших запросов.
    auto_init=True,
    # Автоматическая смена прокси при каждом запросе
    auto_change=False
)
