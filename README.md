# Космический Инстаграм
Это телеграм бот, который получает снимки, сделанные NASA и SpaceX. Это снимки с запуска космических кораблей SpaceX, фото NASA APOD (Astronomy Picture of the Day) и NASA EPIC.
Все снимки мы получаем при помощи API-ключей.

## Как установить
Нам необходимы два API. API SpaceX публичный, потому достаточно просто [перейти к документации](https://documenter.getpostman.com/view/2025350/RWaEzA..) и пользоваться всем необходимым.
Для получения API-ключа NASA нужно уже перейти на [их сайт и зарегистрироваться](https://api.nasa.gov). При помощи этого API-ключа можно получать фото NASA APOD и NASA EPIC.

Сохранять API публично плохая идея. Потому все чувствительные данные стоит скрыть. Для этого в корне репозитория нужно создать ```.env``` файл и поместить ключ туда, прописав:
```python
NASA_API_KEY='Ваш API-ключ'
```

В самом коде это выглядит так:
``` python
NASA_API_KEY = os.getenv('NASA_API_KEY')
```
Ну и наконец необходимо создать телеграм бота в [BotFather](https://telegram.me/BotFather) и получать API-ключ бота и id чата который можно уже указать в ```.env``` файле.
```python
chat_id = 'Ваш chat_id'
```
Для этого папаше ботов нужно прописать команду ```/newbot ``` и придумать боту название и логин (это и есть chat id) заканчивающийся на bot.
API-ключ от телеграм бота необходимо скрыть (на подобии с API NASA).
```python
TGBOT_API_KEY='Ваш API-ключ'
```

В проекте используется пакет [python-dotenv](https://github.com/theskumar/python-dotenv). Он позволяет загружать переменные окружения из файла .env в корневом каталоге приложения.
Этот .env-файл можно использовать для всех переменных конфигурации.
Ну и естественно Python3 должен быть уже установлен. Затем используйте pip (или pip3,если есть конфликт с Python2) для установки зависимостей:
```python
pip install -r requirements.txt
```
## Как пользоваться
Для начала необходимо запустить скрипты ```fetch_nasa.py``` и ```fetch_spacex.py```. Каждый из скриптов попросит ввести имя для папки, которую создаст
(необходимо ввести разные названия для каждой папки). Они создадутся в папке проекта. После каждый из скриптов будет сохранять фото в созданную им же папку. 

После этого запустите скрипт ```send_message.py``` и введите название папки, из которой будут отправляться фото. После всего вышеперечисленного фото будут отправлены в телеграм.

![Launch example](https://user-images.githubusercontent.com/83189636/129692494-49b69876-b261-4815-9106-fca95bcd76c5.PNG )

Пример запуска в консоли
 
