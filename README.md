![Build Status](https://github.com/Andrey-Apa/foodgram-project-react/actions/workflows/foodgram_main.yml/badge.svg)

# Foodgram

«Продуктовый помощник»: сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволяет пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

## Технологии
- Python 3.7.9 и выше
- Django 3.2
- Django REST Framework 3.12.4
- Djoser 2.1.0
- Django filter 22.1
- Gunicorn 20.0.4
- Nginx 1.21.3
- Docker 20.10.22
- Postgres 13.0
- Dotenv 0.21.1

Проект доступен по адресу: http://foodgram-andreyapa.sytes.net/.

Посмотреть список доступных адресов API : http://foodgram-andreyapa.sytes.net/api/.

Документация API доступна по адресу: http://foodgram-andreyapa.sytes.net/api/docs/.

## Запуск проекта локально
1. Склонируйте репозиторий и прейдите в корневую директорию foodgram-project-react:
```bash
git clone git@github.com:Andrey-Apa/foodgram-project-react.git
cd foodgram-project-react
```
2. В директории infra создайте файл с .env с переменными окружения:
```bash
cd infra
```
# Содержание .env 
- DB_ENGINE - движок базы данных # например django.db.backends.postgresql
- DB_NAME - имя базы данных # postgres
- POSTGRES_USER - логин для подключения к базе данных # postgres
- POSTGRES_PASSWORD - пароль для подключения к БД (установите свой) # postgres
- DB_HOST - название сервиса (контейнера) # db
- DB_PORT - порт для подключения к БД # 5432
- SECRET_KEY - секретный ключ
- ALLOWED_HOSTS - разрешенные хосты # localhost

3. Соберите контейнер и запустите:
```bash
docker-compose up --build
```
4. Внутри контейнера backend выполните миграции, загрузите данные, соберите статику:
- выполнить миграции:
```bash
sudo docker-compose exec backend python manage.py migrate
```
- при необходимости загрузите базу данными:
```bash
sudo docker-compose exec backend python manage.py loaddata dump.json
```
- соберите статику:
```bash
sudo docker-compose exec backend python manage.py collectstatic --no-input
```
5. Сооздайте суперюзера:
```bash
sudo docker-compose exec backend python manage.py createsuperuser
```
## Запуск проекта в контейнере
1. Со страницы репозитория https://github.com/Andrey-Apa/foodgram-project-react создать fork проекта в свой GitHUB;

2. В разделе репозитория проекта Setting/Secrets:
- указать логин и пароль вашего DockerHUB с ключами
```bash
DOCKER_USERNAME, DOCKER_PASSWORD
```
- указать параметры сервера для разворачивания проекта (хост, логин, ssh-key, пароль ) с ключами:
```bash
HOST, USER, SSH_KEY, PASSPHRASE
```
- указать параметры базы данных с ключами:
```bash
DB_ENGINE, DB_NAME , POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT
```
- указать ID телеграм-канала и токен телеграм-бота для получения уведомлений с ключами:
```bash
TELEGRAM_TO, TELEGRAM_TOKEN
```
- указать серктеный ключи и разрешенные адреса(через заяпятую) для вашего проекта с ключами:
```bash
SECRET_KEY, ALLOWED_HOSTS
```
3. Подготовить ваш сервер:
- установить докер:
```bash
 sudo apt install docker.io
 ```
- установить docker-compose в соответствии с официальной документацией;
https://docs.docker.com/compose/install/

- cкопировать файлы docker-compose.yaml и nginx.conf из проекта на сервер в home/<ваш_username>/foodgram/docker-compose.yaml и home/<ваш_username>/foodgram/nginx.conf соответственно.

4. На GitHUB выполнить любой commit, для запуска action workflow;

5. На вашем сервере , загрузить данные, собрать статику:
- выполнить миграции:
```bash
sudo docker-compose exec backend python manage.py migrate
```
- при необходимости загрузите базу данными:
```bash
sudo docker-compose exec backend python manage.py loaddata dump.json
```
- создайте суперюзера:
```bash
sudo docker-compose exec backend python manage.py createsuperuser
```
- соберите статику:
```bash
sudo docker-compose exec backend python manage.py collectstatic --no-input
```

6. Ваш проект доступен по адресу вашего сервера:
http://<ip_сервера>/


## Автор backend проекта 
- Андрей Апашкин - https://github.com/Andrey-Apa

## License

MIT

**Free Software, Not for commercial use!**