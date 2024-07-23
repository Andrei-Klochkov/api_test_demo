"""Простое API для проверки доступности имени для регистрации нового пользователя"""

import json
from sys        import path as sys_path
from os         import path as os_path, environ
from datetime   import datetime

from re         import match
from dotenv     import load_dotenv
from flask      import Flask, Response, request

sys_path.append(os_path.abspath(""))
load_dotenv("settings.env")

from data.check_username.result_messages import Messages


app = Flask(__name__)

@app.route("/")
def hello():
    """Функция для проверки работы сервера"""
    return Response(
        json.dumps({"Message": "Hello World!!!"}),
        status=200,
        content_type="application/json",
    )


@app.route("/check-username")
def check_username_api():
    """Функция проверки имени пользователя для регистрации"""

    return_result = ""

    query = request.args
    name  = query["username"]

    response_body = {
        "results": [
            {
                "date": f"{datetime.now()}",
                "function_data": {
                    "params": query,
                    "return": [""],
                },
            }
        ]
    }

    if match(pattern=R"^.+$", string=name) is None:
        return_result = Messages.no_data

    elif match(pattern=R"^[a-z0-9]{1}" , string=name) is None:
        return_result = Messages.incorrect_first_symbol

    elif match(pattern=R"^[a-z0-9\.]+$" , string=name) is None:
        return_result = Messages.incorrect_symbols

    elif match(pattern=R"^.*\.{2,}.*$" , string=name) is not None:
        return_result = Messages.has_double_dot

    elif match(pattern=R"^[0-9/.]{8,}$" , string=name) is not None:
        return_result = Messages.has_eight_symbols_without_letter

    elif match(pattern=R".*[a-z0-9]{1}$" , string=name) is None:
        return_result = Messages.incorrect_last_symbol

    elif match(pattern=R"^.{6,30}$" , string=name) is None:
        return_result = Messages.incorrect_amount_symbols

    else:
        return_result = Messages.success

    response_body["results"][0]["function_data"]["return"][0] = return_result
    return Response(json.dumps(response_body), status=200, content_type="application/json")


if __name__ == "__main__":
    app.run(host=environ["FLASK_HOST"], port=int(environ["PORT"]))
