"""Позитивное функциональное тестирование API check_username"""

from sys    import path as sys_path
from os     import path as os_path

import pytest

sys_path.append(os_path.abspath(""))

from tests.pattern.check_username_api       import CheckUserNameApi
from data.check_username.result_messages    import Messages
from data.check_username.generate_inputs    import DIGITS, LETTERS_LOWER


@pytest.mark.parametrize("input_data", DIGITS)
def test_edges_digits(input_data):
    """Тестирование цифрами"""

    api = CheckUserNameApi(input_data)
    assert api.api_result == Messages.success, "Ошибка: Не получено успешное сообщение"


@pytest.mark.parametrize("input_data", LETTERS_LOWER)
def test_edges_letter_lower(input_data):
    """Тестирование маленькими буквами"""

    api = CheckUserNameApi(input_data)
    assert api.api_result == Messages.success, "Ошибка: Не получено успешное сообщение"
