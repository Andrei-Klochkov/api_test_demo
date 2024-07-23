"""Таблица решений для позитивных входных данных для проверки имени пользователя"""

from sys            import path as sys_path
from os             import path as os_path
from dataclasses    import dataclass

sys_path.append(os_path.abspath(""))

from data.classes               import ColumnDataBase, TableDecision
from tests.functions.data       import get_product


@dataclass(frozen=True)
class PositiveInputValues(ColumnDataBase):
    """Позитивные входные данные для тестирования"""

    first_symbol : tuple = "letter_lower", "digit"
    rest_symbols : tuple = get_product("letter_lower", "digit", "dot")
    last_symbol  : tuple = "letter_lower", "digit"

    def check_data(self, td: TableDecision, i: int):

        if self.rest_symbols == (False, False, False):
            self.block_row(td, i, "Минимальный размер строки 6 символов!")

        if self.rest_symbols == (False, False, "dot"):
            self.block_row(td, i, "Одни точки в остальных символах не допускаются!")


if __name__ == "__main__":
    TableDecision(
        PositiveInputValues(),
        "data/check_username/csv/positive_input_values_raw.csv",
        "data/check_username/csv/positive_input_values_clean.csv"
    )
