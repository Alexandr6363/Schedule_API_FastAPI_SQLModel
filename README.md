# Schedule_API FASTApi + SQLModel


Установка и запуск:

1. Создаем и запускаем витруальнное окружение:
    python -m venv venv
    source venv/bin/activate

2. Устанавливаем зависимости:
    pip install -r requirements.txt

3. Создаем и наполняем тестовую базу данных:
    python create_and_fill_db.py

4. Запускаем: 
    uvicorn main:app --reload

   API достепен по адресу:
        http://127.0.0.1:8000
        http://127.0.0.1:8000/docs