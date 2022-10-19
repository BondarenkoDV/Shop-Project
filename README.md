# Shop-Project

## Реализован следующий функционал:
- Регистрация и аутентификация пользователя
- Личный кабинет пользователя
- Отображение товаров
- Возможность отображать товары по категориям
- Детальная информация о товаре
- Корзина. Можно добавлять товары, также менять их количество и убирать из корзины
- Список избранных товаров, куда можно сохранить товары, а также убирать их оттуда
- Обратная связь с пользователем через почту
- Оплата товара через Stripe

# Настройка
### Склонируйте проект, для этого в терминале введите

`gh repo clone BondarenkoDV/Shop-Project`
### Создайте виртуальное окружение

`python3 -m venv venv`
### Активируйте его:

`source ./venv/bin/activate`
### Установите зависимости

`pip install -r requirements.txt`

### В ShopSite/settings.py замените на свои значения

- EMAIL_HOST
- DEBUG
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD

### Создайте миграции

`python manage.py makemigrations`

`python manage.py migrate`
### Создайте superuser

`python manage.py createsuperuser`
### Запустите

`python manage.py runserver`
