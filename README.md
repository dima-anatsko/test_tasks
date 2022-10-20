### Данный проект предназначен для получения данных о продуктах с сайта  wildberries.
Проект на писан с использованием Django3.2, версия python 3.10, в качестве базы данных используется Postgresql 13.8.
#### Для запуска проекта Вам необходимо: 
1. Склонировать репозиторий себе
2. Активизировать виртуальное окружение: `source myenv/bin/activate`
3. Установить зависимости: `pip install -r requirements.txt`
4. Создать файл .env с настройками проекта (должен располагаться рядом с manage.py)
5. Запустить локальный сервер: `python manage.py runserver`

Пример файла .env:
```text
DEBUG=on
SECRET_KEY=your_secret_key
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=your_db_host
DATABASE_PORT=your_db_port
```
___

#### Пример запроса для получения данных по артиклю:
```  
curl --location --request POST 'http://127.0.0.1:8000/wildberries/products' \  
--header 'Content-Type: application/json' \  
--data-raw '{"article": "73508252"}'  
```
Пример ответа:
```json
{
    "article": 73508252, 
    "brand": "Мир Фигурного Катания",
    "title": "Аксессуар для коньков"
}
```
___

#### Пример запроса для получения данных по списку артиклей из excel файла:
В первом столбце на первом листе должны быть указаны артикли нужных товаров:  
```  
curl --location --request POST 'http://127.0.0.1:8000/wildberries/products' \  
--header 'Content-Disposition: attachment; filename="articles.xlsx"' \  
--header 'Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' \  
--data-binary '@/home/user/files/articles.xlsx'  
```
Пример ответа:
```json
[
    {
        "article": 73508252,
        "brand": "Мир Фигурного Катания",
        "title": "Аксессуар для коньков"
    },
    {
        "article": 17272715,
        "brand": "Rabby",
        "title": "Комплекты БДСМ / 10 шт."
    },
    {
        "article": 46090851,
        "brand": "Luckybox",
        "title": "Подарок папе мужчине отцу сладкий бокс"
    }
]
```
