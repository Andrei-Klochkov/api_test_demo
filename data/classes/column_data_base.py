"""Базовый класс для колонок таблицы решений"""

from __future__         import annotations
from typing             import TYPE_CHECKING
from dataclasses        import dataclass
from abc                import ABC, abstractmethod

if TYPE_CHECKING:
    from sys            import path as sys_path
    from os             import path as os_path

    sys_path.append(os_path.abspath(""))

    from data.classes   import TableDecision


@dataclass(frozen=True, init=True)
class ColumnDataBase(ABC):
    """Базовый класс для колонок таблицы решений"""

    @abstractmethod
    def check_data(self, td: TableDecision, i: int):
        """Проверка данных"""

    def block_row(self, td: TableDecision, i:int, msg: str):
        """Отбраковка строки"""

        td.blocked[i]  = True
        td.reason[i]  += msg
        td.reason[i]  += "\n" * 2

    def check_both(self, condition_1: bool, condition_2: bool) -> bool:
        """Проверка условия в обе стороны"""

        if (condition_1 and not condition_2) or (not condition_1 and condition_2):
            return False

        return True
