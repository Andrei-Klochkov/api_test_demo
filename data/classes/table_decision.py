"""Таблица решений"""

from __future__     import annotations
from typing         import TYPE_CHECKING
from itertools      import product
from pandas         import DataFrame

if TYPE_CHECKING:
    from sys            import path as sys_path
    from os             import path as os_path

    sys_path.append(os_path.abspath(""))

    from data.classes.column_data_base import ColumnDataBase


class TableDecision():
    """Таблица решений"""

    def __init__(
        self, col_data: ColumnDataBase, csv_raw: str = None, csv_clean: str = None
    ) -> None:

        self.col_data   = col_data
        self.clean_rows = []

        values             = col_data.__dict__.values()
        cartesian          = product(*values)
        zipped             = zip(*cartesian)
        self.cart_col_data = col_data.__class__(*zipped)

        row_amount = len(self.cart_col_data.__dict__[next(iter(self.cart_col_data.__dict__))])

        self.blocked    = [False]   * row_amount
        self.reason     = [""]      * row_amount

        for i, row in enumerate(zip(*self.cart_col_data.__dict__.values())):
            col_data_row: ColumnDataBase = col_data.__class__(*row)
            col_data_row.check_data(self, i)

            if self.blocked[i] is False:
                self.clean_rows.append(row)

        self.__csv_export(csv_raw, csv_clean)

    def __csv_export(self, csv_raw: str, csv_clean: str):
        """Экспорт данных в csv"""

        index_name = "[№]"

        if csv_raw is not None:
            raw_data_dict              = self.cart_col_data.__dict__
            raw_data_dict["[blocked]"] = self.blocked
            raw_data_dict["[reason]"]  = self.reason

            df_raw = DataFrame(data = self.cart_col_data.__dict__)
            df_raw.index.name = index_name
            df_raw.to_csv(csv_raw)

        if csv_clean is not None:
            clean_col_data      = self.col_data.__class__(*zip(*self.clean_rows))
            df_clean            = DataFrame(data=clean_col_data.__dict__)
            df_clean.index.name = index_name
            df_clean.to_csv(csv_clean)
