1. виртуальное окружение и пакеты:
```
python -m venv env
pip install -r requirements.txt
```

2. базы db (пока так):
запускаем интерпретатор Python внутри env:  
```
python
```
Внутри интерпретатора для инициализации:
```python
import services
services.createdatabase()
exit()
```

3. run сервер:
   
```
uvicorn main:app --reload
```
