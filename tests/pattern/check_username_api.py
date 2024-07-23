"""Тестируемый API"""

from sys                        import path as sys_path
from os                         import path as os_path, environ
import requests
from requests                   import Response
from dotenv                     import load_dotenv

sys_path.append(os_path.abspath(""))
load_dotenv("settings.env")

from tests.pattern.base_api     import BaseApi


class CheckUserNameApi(BaseApi):
    """Класс для check_name API"""

    @property
    def api_result(self):
        """Результат API"""

        return self.__api_result

    def __init__(self, username_data) -> None:

        main_url = f"http://{environ["TEST_HOST"]}"
        port     = environ["PORT"]
        func     = "check-username"
        url      = f"{main_url}:{port}/{func}"
        query    = {"username": username_data}

        url = f"{main_url}:{port}/{func}"
        response: Response = requests.get(
            url=url, params=query, headers=self.headers, timeout=self.base_timeout
        )
        super().__init__(response)

        self.__api_result = self.__get_api_result()

    def __get_api_result(self) -> str:
        """Функция для получения результата API"""

        path    = R"$.results[0].function_data.return[0]"
        value   = self.parse_json(path)

        assert len(value)  == 1                    , "Количество элементов не равно 1!"
        assert isinstance(value[0], str)           , "Тип значения отличается от str!"

        return str(value[0])
