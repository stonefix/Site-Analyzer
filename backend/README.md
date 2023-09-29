1. виртуальное окружение и пакеты:
```
python -m venv env
pip install -r requirements.txt
```

2. базы db (пока так):
```
python
```
В интерпретаторе, в виртуальном окружении env, для инициализации:
```python
import services
services.create_database()
```

3. run сервер:
   
```
uvicorn main:app --reload
```
