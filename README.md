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

Проект доступен по адресу: https://foodgram-andreyapa.sytes.net/.

Посмотреть список доступных адресов API : https://foodgram-andreyapa.sytes.net/api/.

Документация API доступна по адресу: https://foodgram-andreyapa.sytes.net/api/docs/.

## Запуск проекта локально
1. Склонируйте репозиторий и прейдите в директорию backend:
```bash
git clone git@github.com:Andrey-Apa/foodgram-project-react.git

cd backend
```
2. Cоздать и активировать виртуальное окружение:
-для Windows
```bash
python -m venv venv
. venv/Scripts/activate
```
-для Linux, MacOs:
```bash
python3 -m venv venv
source env/bin/activate
```
3. Обновите pip и установите зависимости из файла requirements.txt:
-для Windows
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
-для Linux, MacOs:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Выполнить миграции:
Выполнить миграции из директории foodgram:
-для Windows:
```bash
cd foodgram/
python manage.py migrate
```
-для Linux, MacOs:
```bash
cd foodgram/
python3 manage.py migrate
```
5. Загрузите базу данными ингридиентов:
-для Windows:
```bash
cd ../data
python manage.py loaddata ingredients.json
```
-для Linux, MacOs:
```bash
cd ../data
python3 manage.py loaddata ingredients.json
```
6. Запустить проект:
-для Windows
```bash
cd ../backend
python manage.py runserver
```
-для Linux, MacOs:
```bash
cd ../backend
python3 manage.py migrate
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

4. На GitHUB выполнить любой commit, для запуска action workflow;

5. На вашем сервере , загрузить данные, собрать статику:
- выполнить миграции:
```bash
sudo docker-compose exec web python manage.py migrate
```
- при необходимости загрузите базу данными:
```bash
sudo docker-compose exec web python manage.py loaddata ingredients.json
```
- создайте суперюзера:
```bash
sudo docker-compose exec web python manage.py createsuperuser
```
- соберите статику:
```bash
sudo docker-compose exec web python manage.py collectstatic --no-input
```

6. Ваш проект доступен по адресу вашего сервера:
http://<ip_сервера>/


## Автор backend проекта 
- Андрей Апашкин - https://github.com/Andrey-Apa

## License

MIT

**Free Software, Not for commercial use!**