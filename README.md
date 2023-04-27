# Описание проекта YaMDb_api

YaMDb - сервис, позволяющий писать и читать отзывы на фильмы, книги, картины и т.д.
Этот репозиторий - API проекта YaMDb.

### Технологии

Python 3.7 | Django 3.2.16 | Django REST Framework 3.12.4 | Simple JWT 4.7.2

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MiladyEmily/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Как использовать

Вот как можно зарегистрироваться и написать отзыв.
1. Отправляем POST запрос на эндпоинт /auth/signup/, передавая почту и имя пользователя в тело запроса, например:
```json
{
    "email": "bestreviewer152@yandex.ru",
    "username": "bestreviewer"
}
```
2. После этого на почту должен прийти код подтверждения, копируем его и отправляем POST запрос на эндпоинт /auth/token/, передавая имя пользователя и код подтверждения в тело запроса, например:
```json
{
    "username": "bestreviewer",
    "confirmation_code": "71fdf3ab"
}
```
3. Получаем JWT токен, в заголовках следующих запросов добавляем `Authorization: Bearer ТОКЕН_ПОЛЬЗОВАТЕЛЯ` .
4. Читаем документацию и спокойно пользуемся сервисом. :)

### Авторы:

- https://github.com/gusevskiy
- https://github.com/MiladyEmily
- https://github.com/timaaos
