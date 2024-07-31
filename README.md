# Приложение для отображения погоды

### Приложение предазначено для вывода информации о времени и текущей погоде в 6 разных городах. Также реализована возможность отображения бегущей строки с новостями, которые загружаются по RSS ссылке с любого новостного портала.


### Как запустить проект:

Сделать форк репозитория

Клонировать репозиторий, заменив username на имя пользователя и перейти в него в командной строке:

```
git clone git@github.com:username/hdlt_test_case.git
```

```
cd hdlt_test_case
```

Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В файле get_weather.py заменить значение переменной API_TOKEN на актуальный токен сервиса Яндекс Погода. Токен можно получить на сайте: https://yandex.ru/dev/weather/

В файле newsfeed.py заменить значение переменной RSS_URL на RSS ссылку желаемого новостного портала, например:

```
RSS_URL = 'http://static.feed.rbc.ru/rbc/logical/footer/news.rss'
```

В файле main.py изменить названия городов и их координаты в переменной cities. Координаты необходимо задавать в пределах от -90 до 90 для широты и от -180 до 180 для долготы. Пример:

```
cities = [
    ('КАЛИНИНГРАД', 54.71173, 20.5088),
    ('СОЧИ', 43.584469, 39.720280)
    ('МОСКВА', 55.74663, 37.62144),
    ('ЕКАТЕРИНБУРГ', 56.83883, 60.60002),
    ('ОМСК', 54.989811, 73.374413),
    ('ВЛАДИВОСТОК', 43.11978, 131.88861),
]
```

Для определения координат можно воспользоваться данным сервисом https://www.latlong.net

При необходимости можно заменить базовые изображения фона и текущей погоды в директории assets. Фоновые изображения должны находится в директории backgrounds. Изображения погодных условий в директории weather_cond. Изображения должны бать в формате .jpg и соответсвовать разрешению, для фоновых изображений 266х300, для изображений погодных условий 75х75. В каждой из директорий должно быть 5 файлов с соответсвующими названиями: clear.jpg, cloudy.jpg, overcast.jpg, rain.jpg, snow.jpg

Образец:

    ├── assets                       # Директория с изображениями
    │   ├── backgrounds              # Директория для изображений фона
    │   │   ├── clear.jpg
    │   │   ├── cloudy.jpg
    │   │   ├── overcast.jpg
    │   │   ├── rain.jpg
    │   │   └── snow.jpg
    |   ├── weather_cond             # Директория для изображений текущей погоды
    │   │   ├── clear.jpg
    │   │   ├── cloudy.jpg
    │   │   ├── overcast.jpg
    │   │   ├── rain.jpg
    │   │   └── snow.jpg        

Для запуска проекта выполнить команду в основной дериктории проекта:

```
python main.py
```

Также обратить внимание на то, что температура воздуха и температура по ощущениям имеют одинаковые значния, поскольку в приложении используется бесплатный тариф Яндекс Погоды, который не предоставлет информации о температуре по ощущениям.
