"""
    Дана таблица всех доступных продуктов на складе.
    Данные представлены в виде списка словарей (a list of dicts)

    Ваша миссия тут - это найти ТОП самых дорогих товаров.
    Количество товаров, которые мы ищем, будет передано в первом аргументе,
    а сами данные по товарам будут переданы вторым аргументом.

    Вх. данные: Число и список словарей (int and list of dicts).
    Каждый словарь имеет 2 ключа "name" и "price".

    Вых. данные: Такой же как и второй аргумент.
"""


def bigger_price(count: int, lst_f_dct: list) -> list:
    prices = [dct.get("price") for dct in lst_f_dct]
    prices.sort(reverse=True)
    new = []
    for i in range(count):
        for j in range(len(lst_f_dct)):
            if lst_f_dct[j].get("price") == prices[i]:
                new.append(lst_f_dct[j])
                break
    return new
