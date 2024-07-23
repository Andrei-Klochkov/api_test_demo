"""Генерация входящих данных для проверки имени пользователя"""

from sys            import path as sys_path
from os             import path as os_path, environ

from pandas         import DataFrame
from dotenv         import load_dotenv

sys_path.append(os_path.abspath(""))
load_dotenv("settings.env")

from tests.functions.data import generate_data, generate_data_edges, get_data

AMOUNT             = 1
MAIN_PATH          = environ["CHECK_USERNAME_INPUTS"]
DIGITS_PATH        = MAIN_PATH + "digits.csv"
LETTERS_LOWER_PATH = MAIN_PATH + "letters_lower.csv"

DIGITS        = get_data(DIGITS_PATH)
LETTERS_LOWER = get_data(LETTERS_LOWER_PATH)


if __name__ == "__main__":

    digits =\
        generate_data_edges(e=(4, 5, 27, 28), p="^[abyz]{1}[0189]{<n>}[0189]{1}$", a=AMOUNT) + \
        generate_data_edges(e=(4, 5, 27, 28), p="^[abyz]{1}[0189]{<n>}[abyz]{1}$", a=AMOUNT) + \
        generate_data_edges(e=(4, 5, 27, 28), p="^[0189]{1}[0189]{<n>}[abyz]{1}$", a=AMOUNT) + \
        generate_data_edges(e=(4, 5)        , p="^[0189]{1}[0189]{<n>}[0189]{1}$", a=AMOUNT)

    letters_lower =\
        generate_data_edges(e=(4, 5, 27, 28), p="^[abyz]{1}[abyz]{<n>}[0189]{1}$", a=AMOUNT) + \
        generate_data_edges(e=(4, 5, 27, 28), p="^[abyz]{1}[abyz]{<n>}[abyz]{1}$", a=AMOUNT) + \
        generate_data_edges(e=(4, 5, 27, 28), p="^[0189]{1}[abyz]{<n>}[abyz]{1}$", a=AMOUNT) + \
        generate_data_edges(e=(4, 5, 27, 28), p="^[0189]{1}[abyz]{<n>}[0189]{1}$", a=AMOUNT)

    DataFrame(digits)       .to_csv(DIGITS_PATH         , index=False, header=False)
    DataFrame(letters_lower).to_csv(LETTERS_LOWER_PATH  , index=False, header=False)




