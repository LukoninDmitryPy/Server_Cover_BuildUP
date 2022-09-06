# Проект YaCut 
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![REST API](https://img.shields.io/badge/-REST%20API-464646?style=flat-square&logo=REST%20API)](https://restfulapi.net/)
[![SQLite](https://img.shields.io/badge/-SQLite-464646?style=flat-square&logo=SQLite)](https://www.sqlite.org/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)

Cover_build_up реализован загрузки, хранения и выгрузки xslx файлов с полями Unit, Reach% (1-10)+.

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone https://github.com/LukoninDmitryPy/server_cover_build_up
```

### Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

### Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Запуск проекта:

```
py manage.py runserver
```

### Работа с API через Postman Agent:

#### Для регистрации и аутентификации:

```
POST http://127.0.0.1:8000/users/
```
```
JSON:
{
    "username": "user",
    "password": "user1234"
} 
```
    
```
POST http://127.0.0.1:8000/jwt/create/
```
```
JSON:
{
    "username": "user",
    "password": "user1234"
} 
```

#### Работа с загрузкой XLSX документа в базу данных:

```
POST http://127.0.0.1:8000/v1/users/
```
```
JSON:
{
    Authorization:"Token 'access-token'"
} 
```

#### Получение данных ответом:

```
GET http://127.0.0.1:8000/v1/users/
```
```
JSON:
{
    Authorization:"Token 'access-token'"
} 
```

#### Работа с выгрузкой данных в xslx документ:

```
GET http://127.0.0.1:8000/v1/users/download_and_get/
```
```
JSON:
{
    Authorization:"Token 'access-token'"
} 
```
* Для получения xslx файла, необходимо переместить файл raw_data.txt в папку cover_buildup

* ВЫполнить повторный GET запрос

# Над проектом работал
- [Дмитрий Луконин](https://wa.me/79153612056)
