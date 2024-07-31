### Запуск сервиса локально


1. Установить `docker-compose`
2. Установить `python` версии 3.10.6 (можно использовать [pyenv](https://github.com/pyenv/pyenv))
3. Установить `poetry`
4. Создать виртуальное окружение через `venv`
5. Установить пакеты: `poetry install`
6. Поднять базу в докере: `docker-compose up`
7. Запустить миграции: `alembic upgrade head`
8. Заполнить тестовыми данными базу: `python load_data.py`




