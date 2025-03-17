# Schedule_API FASTApi + SQLModel


## Установка и запуск. (Без docker):

### 1. Создаем и запускаем витруальнное окружение:
   
    python3 -m venv venv
    source venv/bin/activate

### 2. Устанавливаем зависимости:
   
    pip install -r requirements.txt

### 3. Создаем и наполняем тестовую базу данных:
   
    python3 create_and_fill_db.py

### 4. Запускаем:
   
    uvicorn main:app --reload

## Установка и запуск. (С docker):

### 1. Создаем образ и запускаем контейнер:

docker build -t api .

docker run --name api -p 8000:80 api

## API достепен по адресу:
   
http://127.0.0.1:8000  

## Интерактивная документация API:
  
http://127.0.0.1:8000/docs
