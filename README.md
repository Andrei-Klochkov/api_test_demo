Демонстрационный проект тестирования API.

Сборка и запуск в Docker из root-каталога проекта:
	docker build -t simple_api_img -f app/Dockerfile .
	docker build -t tests_for_simple_api_img -f tests/Dockerfile .
  
	docker run -it -p 5000:5000 --name simple_api_cont simple_api_img
	docker run -it --link simple_api_cont:simple_api_app --name tests_for_simple_api_cont tests_for_simple_api_img
