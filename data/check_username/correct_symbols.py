"""Таблица решений входных данных для проверки имени пользователя"""

from sys            import path as sys_path
from os             import path as os_path
from dataclasses    import dataclass

sys_path.append(os_path.abspath(""))

from data.classes   import ColumnDataBase, TableDecision


@dataclass(frozen=True)
class BlockMessages():
    """Сообщения для отбраковки"""

    only_dots: str = "Одни точки в имени пользователя не допускаются"
    no_data  : str = "Должны быть хоть какие-то данные"


@dataclass(frozen=True)
class PositiveInputData(ColumnDataBase):
    """Входные данные для тестирования"""

    letters_lower : tuple = True, False
    digits        : tuple = True, False
    dots          : tuple = True, False

    def check_data(self, td: TableDecision, i: int):

        match self:
            case s if s.dots is True and s.letters_lower is False and s.digits is False:
                s.block_row(td, i, BlockMessages.only_dots)

            case s if s.dots is False and s.letters_lower is False and s.digits is False:
                s.block_row(td, i, BlockMessages.no_data)


if __name__ == "__main__":
    TableDecision(
        PositiveInputData(),
        "data/check_username/csv/correct_symbols_raw.csv",
        "data/check_username/csv/correct_symbols_clean.csv",
    )
