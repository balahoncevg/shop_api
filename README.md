# Магазин продуктов на Django

## Описание

Это API проекта магазина продуктов. API позволяет работать с категориями, подкатегориями, продуктами и корзиной покупок.Операции с корзиной могут выполнять только авторизованные пользователи.

## Стек технологий

- Django
- Django Rest Framework
- Sqlite3
- Djoser
- Unittest

## Инструкция по запуску

### 1. Клонировать репозиторий
```
git clone https://github.com/balahoncevg/shop_api.git
```

### 2. Установить зависимости
```
pip install -r requirements.txt
```

### 3. Выполнить миграции
```
python manage.py migrate
```

### 4. Загрузить фикстуры
```
python manage.py loaddata products/fixtures/shop_data.json
```

### 5. Запустить сервер
```
python manage.py runserver
```

## Документация к API

http://127.0.0.1:8000/swagger/

## Тесты
```
python manage.py test api
```