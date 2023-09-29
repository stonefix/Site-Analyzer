1. виртуальное окружение и пакеты:

python -m venv env
pip install -r requirements.txt

базы db (пока так):

запускаем python для инициализации

import services
services.create_database()


run сервер:

uvicorn main:app --reload