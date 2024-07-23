"""Таблица решений для проверки имени пользователя"""

from sys            import path as sys_path
from os             import path as os_path
from dataclasses    import dataclass

sys_path.append(os_path.abspath(""))

from data.classes import TableDecision, ColumnDataBase


@dataclass(frozen=True)
class ResultMessages():
    """Сообщения для результата"""

    success                          : str = "Успех"
    no_data                          : str = "Нет данных"
    incorrect_first_symbol           : str = "Недопустимый первый символ"
    incorrect_symbols                : str = "Недопустимые символы"
    has_double_dot                   : str = "Есть 2 точки подряд"
    has_eight_symbols_without_letter : str = "8+ допустимых символов без букв"
    incorrect_last_symbol            : str = "Недопустимый последний символ"
    incorrect_amount_symbols         : str = "Недопустимое количество символов"


@dataclass(frozen=True)
class BlockMessages():
    """Сообщения для отбраковки"""

    possible_success                : str = (
        "Если все проверки успешны, то всегда успех. Если не все, то всегда ошибка"
    )

    no_data                         : str = (
        "Если нет данных, то всегда ошибка данных, дальше не проверяем"

    )

    correct_first_symbol            : str = (
        "Если первый символ некорректный, то ошибка первого символа, дальше не проверяем"
    )

    correct_symbols                 : str = (
        "Если есть некорректные символы, то ошибка некорректных символов, дальше не проверяем"
    )

    no_double_dot                   : str = (
        "Если есть точки подряд, то ошибка точек подряд, дальше не проверяем"
    )

    no_eight_symbols_without_letter : str = (
        "Если 8+ символов без букв, то ошибка 8+ символов без букв, дальше не проверяем"
    )

    correct_last_symbol             : str = (
        "Если последний символ некорректный, то ошибка последнего символа, дальше не проверяем"
    )

    correct_amount_symbols          : str = (
        "Если недопустимое количество символов, то ошибка количества символов"
    )


@dataclass(frozen=True)
class ColumnData(ColumnDataBase):
    """Колонки для таблицы решений"""

    any_data                        : tuple = True, False
    correct_first_symbol            : tuple = True, False
    correct_symbols                 : tuple = True, False
    no_double_dot                   : tuple = True, False
    no_eight_symbols_without_letter : tuple = True, False
    correct_last_symbol             : tuple = True, False
    correct_amount_symbols          : tuple = True, False

    result                          : tuple = tuple(ResultMessages().__dict__.values())

    def check_data(self, td: TableDecision, i):
        """Проверка данных"""

        match self:
            case s if s.check_both(
                all(tuple(s.__dict__.values())[:-1]), s.result != ResultMessages.success
            ):
                s.block_row(td, i, BlockMessages.possible_success)

            case s if s.check_both(
                s.any_data is True, s.result == ResultMessages.no_data
            ):
                s.block_row(td, i, BlockMessages.no_data)

            case s if s.check_both(
                s.correct_first_symbol is True, s.result == ResultMessages.incorrect_first_symbol
            ):
                s.block_row(td, i, BlockMessages.correct_first_symbol)

            case s if s.check_both(
                s.correct_symbols is True, s.result == ResultMessages.incorrect_symbols
            ):
                s.block_row(td, i, BlockMessages.correct_symbols)

            case s if s.check_both(
                s.no_double_dot is True, s.result == ResultMessages.has_double_dot
            ):
                s.block_row(td, i, BlockMessages.no_double_dot)

            case s if s.check_both(
                s.no_eight_symbols_without_letter is True,
                s.result == ResultMessages.has_eight_symbols_without_letter,
            ):
                s.block_row(td, i, BlockMessages.no_eight_symbols_without_letter)

            case s if s.check_both(
                s.correct_last_symbol is True, s.result == ResultMessages.incorrect_last_symbol,
            ):
                s.block_row(td, i, BlockMessages.correct_last_symbol)

            case s if s.check_both(
                s.correct_amount_symbols is True,
                s.result == ResultMessages.incorrect_amount_symbols,
            ):
                s.block_row(td, i, BlockMessages.correct_amount_symbols)


if __name__ == "__main__":

    TableDecision(
        ColumnData(),
        "data/check_username/csv/common_raw.csv",
        "data/check_username/csv/common_clean.csv",
    )
