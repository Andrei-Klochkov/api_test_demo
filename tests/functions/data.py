"""Функция для работы с данными"""

from itertools          import chain, product

from exrex              import getone
import pandas as pd


def get_data(fullpath: str):
    """Функция для получения данных из CSV"""
    result = []

    try:
        result = list(chain(*pd.read_csv(fullpath).values.tolist()))
    except Exception:
        pass

    return result


def generate_data(p: str, n: int = 1):
    """Генератор данных"""

    for _ in range(n):
        yield getone(p)


def get_product(*data: str) -> tuple:
    """Получить кортеж всех комбинаций из кортежа строк"""

    return tuple(product(*chain((i, False) for i in data)))


def generate_data_edges(e: tuple[int, ...], p: str, a=1):
    """Генерация граничных данных, в паттерне нужен \"<n>\"!!!"""

    return tuple(
        data
        for numb in e
        for data in generate_data(
            p=p.replace("<n>", f"{numb}"), n=a
        )
    )
