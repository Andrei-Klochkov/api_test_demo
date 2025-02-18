# Демонстрационный проект тестирования API.
### Описание:
API проверяет доступность имени пользователя для регистрации. API принимает единственный аргумент с именем пользователя и возвращает сообщение с результатом.

### Сборка и запуск в Docker из root-каталога проекта:

	docker build -t simple_api_img -f app/Dockerfile .
	docker build -t tests_for_simple_api_img -f tests/Dockerfile .
  
	docker run -it -p 5000:5000 --name simple_api_cont simple_api_img
	docker run -it --link simple_api_cont:simple_api_app --name tests_for_simple_api_cont tests_for_simple_api_img

```mermaid
sequenceDiagram

	autonumber

    participant Client
    participant Backend


	Client->>+Backend: Запрос со значением имени пользователя
    alt Отправлено пустое значение
        Backend-->>Client: Ошибка: Введите имя пользователя!

	else Недопустимое количество символов?
		Backend-->>Client: Ошибка: Имя пользователя должно содержать от 6 до 30 символов!

	else Есть недопустимые символы
		Backend-->>Client: Ошибка: Извините, но допускаются только<br>латинские буквы (a-z), цифры (0-9) и точки (.)!

    else Недопустимый первый символ
        Backend-->>Client: Ошибка: Первый символ в имени пользователя должен быть<br>буквой (a–z) или цифрой (0–9) из таблицы ASCII!

	else Есть точки подряд
		Backend-->>Client: Ошибка: В имени пользователя не должно быть нескольких точек (.) подряд!

	else 8+ символов без букв
		Backend-->>Client: Ошибка: Извините, но имя пользователя, состоящее из 8 или более символов, <br>должно включать хотя бы одну латинскую букву (a-z)!

	else Недопустимый последний символ
		Backend-->>Client: Ошибка: Последний символ в имени пользователя должен быть<br>буквой (a–z) или цифрой (0–9) из таблицы ASCII!

	else Имя пользователя уже используется
		Backend-->>Client: Ошибка: Это имя пользователя уже используется. Попробуйте другое.

	else Все ок?
		Backend-->>-Client: Успешно: Имя пользователя доступно для регистрации!
    end
```