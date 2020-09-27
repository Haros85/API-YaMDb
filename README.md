[![Continuous Integration YaMDB Actions Status](https://github.com/{popperony}/{yamdb_final}/workflows/{yamdb.yaml}/badge.svg)](https://github.com/{popperony}/{yamdb_final}/actions)
# Проект "YaMDb"
Проект "**YaMDb**" — база отзывов пользователей о фильмах, книгах и музыке.  
Задача проекта - создание API для организации доступа к базе отзывов о фильмах, книгах и музыке.  

С помощью API, можно получить доступ к следующим ресурсам:
* TITLES: произведения, к которым пишут отзывы (просмотр, создание, редактирование, удаление)
* CATEGORIES: категории (типы) произведений (просмотр, создание, редактирование, удаление)
* GENRES: жанры произведений (просмотр, создание, редактирование, удаление)
* REVIEWS: отзывы на произведения (просмотр, создание, редактирование, удаление)
* COMMENTS: комментарии к отзывам (просмотр, создание, редактирование, удаление)
* AUTH: аутентификация (Получение JWT-токена в обмен на email и confirmation_code)
* USERS: пользователи (просмотр, создание, редактирование, удаление)
  
## Пользовательские роли  
* **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.  
* **Аутентифицированный пользователь** — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить рейтинг произведениям (фильмам/книгам/песням), может комментировать чужие отзывы и ставить им оценки; может редактировать и удалять свои отзывы и комментарии.  
* **Модератор** — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.  
* **Администратор** — полные права на управление проектом и всем его содержимым. Может создавать и удалять категории и произведения. Может назначать роли пользователям.  
* **Администратор Django** — те же права, что и у роли Администратор.  

## Алгоритм регистрации пользователей  
1. Пользователь отправляет запрос с параметром email на /auth/email/.  
2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.  
3. Пользователь отправляет запрос с параметрами email и confirmation_code на /auth/token/, в ответе на запрос ему приходит token (JWT-токен).  
4. При желании пользователь отправляет PATCH-запрос на /users/me/ и заполняет поля в своём профайле (описание полей — в документации).  

## Установка
Для установки на локальной машине потребуется:
* Скачать файлы проекта из репозитория
* Установить и настроить Docker

## Запуск приложения
В корневом каталоге проекта необходимо собрать образ из прилагающегося dockerfile.
Для этого используем команду:
````
docker-compose build
````
После успешного выполнения команды, присутпаем к запуску приложения:
````
docker-compose up
````
Далее необходимо войти в контейнер Web для настройки приложения
Узнаем ID_контейнера web командой:
````
 docker container ls -a
````
Заходим в контейнер web:
````
docker exec -ti id_контейнера bash
````
Осщуествим миграции, тем самым удостоверимся о подключении приложения к базе данных Postgres:
````
python manage.py migrate
````
Создадим суперпользователя:
````
python manage.py createsuperuser
````
Загружаем подготовленные данные для нашего приложения:
````
python manage.py loaddata fixtures.json
````
Приложение запущено и готово к использованию.

## API
Передача данных осуществляется по протоколу HTTP.  
Применяются принципы REST API.  
Сервер отвечает в формате JSON.  
Аутентификация осуществляется по JWT-токену.  
Адрес API: http://localhost:8000/api/v1/  
Документация с примерами команд: http://localhost:8000/redoc/  
## Несколько примеров использования API
**GET /titles/** - получить список всех произведений  
Ответ (200):  
Ключ|Значение|Описание
----|--------|--------
"id"|number|ID произведения
"name"|"string"|Название
"year"|number|Год выпуска
"rating"|number|Рейтинг на основе отзывов
"description"|"string"|Описание
"genre"|Array of objects|Жанр
||"name"|Название жанра
||"slug"|Поле "slug" 
"category"|objects|Категория
||"name"|Название категории объекта
||"slug"|Поле "slug" 
  
**POST /auth/email/** - передача confirmation_code на адрес эл.почты  
Запрос:  
Ключ|Значение|Описание
----|--------|--------
email|"string"|адрес эл.почты

В результате выполнения этого запроса, пользователь получает на указанный адрес эл.почты код подтверждения __confirmation_code__  

**POST /auth/token/** - получение JWT-токена в обмен на email и confirmation_code  
Запрос:  
Ключ|Значение|Описание
----|--------|--------
email|"string"|адрес эл.почты
confirmation_code|"string"|код подтверждения

**PATCH /users/me/** - изменить данные своей учетной записи  
Запрос:  
Ключ|Значение|Описание
----|--------|--------
"first_name"|"string"|Имя
"last_name"|"string"|Фамилия
"username"|"string"|Username
"bio"|"string"|О себе
"email"|"string"|Адрес электронной почты
"role"|"string"| Enum: "user" "moderator" "admin"  

Ответ (200):
Ключ|Значение|Описание
----|--------|--------
"first_name"|"string"|Имя
"last_name"|"string"|Фамилия
"username"|"string"|Username
"bio"|"string"|О себе
"email"|"string"|Адрес электронной почты
"role"|"string"| Enum: "user" "moderator" "admin"  


__**Более подробную информацию о методах данного API можно получить по адресу http://localhost:8000/redoc/**__

