"""Базовый класс API"""

import json

from abc                import ABC
from jsonpath_ng.ext    import parser
from requests           import Response


class BaseApi(ABC):
    """Базовый класс для API"""

    @property
    def headers(self):
        """Базовые заголовки"""

        return {"Accept": "application/json; charset=UTF-8"}

    @property
    def base_timeout(self):
        """Базовый таймаут"""

        return 1

    def __init__(self, response: Response) -> None:
        self.response: Response = response
        assert 200 <= self.response.status_code <= 299, "Не получен успешный статус-код!"

    def parse_json(self, json_path: str) -> list:
        """Функция для парсинга JSON-ответа"""

        match = parser.parse(json_path).find(json.loads(self.response.text))

        return [i.value for i in match]
