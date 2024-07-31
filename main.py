import pytz
from datetime import datetime
from tkinter import Tk, Canvas, StringVar, Label
from timezonefinder import TimezoneFinder

from get_weather import get_weather, get_pictures
from newsfeed import make_newsfeed

WIDGET_COORDINATES = [(0, 0), (266, 0), (532, 0),
                      (798, 0), (1064, 0), (1330, 0)]
TIME_FONT = ('Arial Black', 40)
SMALL_FONT = ('Arial Black', 15)
BIG_FONT = ('Arial Black', 20)
SMALLEST_FONT = ('Arial Black', 10)

WIND_DIRECTION = {
    'CALM': 'Штиль',
    'NORTH': 'С',
    'NORTH_EAST': 'СВ',
    'EAST': 'В',
    'SOUTH_EAST': 'ЮВ',
    'SOUTH': 'Ю',
    'SOUTH_WEST': 'ЮЗ',
    'WEST': 'З',
    'NORTH_WEST': 'СЗ',
}

CLOUDINESS = {
    'CLEAR': 'Ясно',
    'PARTLY': 'Переменная \n облачность',
    'SIGNIFICANT': 'Облачно \n с прояснениями',
    'CLOUDY': 'Облачно',
    'OVERCAST': 'Пасмурно',
}


cities = [
    ('КАЛИНИНГРАД', 54.71173, 20.5088),
    ('СОЧИ', 43.584469, 39.720280),
    ('МОСКВА', 55.74663, 37.62144),
    ('ЕКАТЕРИНБУРГ', 56.83883, 60.60002),
    ('ОМСК', 54.989811, 73.374413),
    ('ВЛАДИВОСТОК', 43.11978, 131.88861),
]

citiesCanvases = []

root = Tk()
root.geometry('1600x300')

svar = StringVar()
labl = Label(root, textvariable=svar, height=10)

root.resizable(width=False, height=False)


class CityCanvas(Canvas):

    def __init__(self, master, city, lat, lon):
        Canvas.__init__(self, master, width=266, height=280)
        self.city = city
        self.lat = lat
        self.lon = lon
        self.create_widget()

    def get_time(self):
        time_zone = TimezoneFinder().timezone_at(lat=self.lat, lng=self.lon)
        time = datetime.now(pytz.timezone(time_zone))
        time = time.strftime('%H:%M')
        return time

    def get_weather(self):
        return get_weather(self.lat, self.lon)

    def get_image(self, weather):
        bg, weather_cond = get_pictures(weather)
        self.bg = bg
        self.weather_cond = weather_cond
        return bg, weather_cond

    def work_time_color(self, time):
        hour = int(time.split(':')[0])
        if hour >= 9 and hour < 18:
            return 'green'
        return 'yellow'

    def create_widget(self):
        time = self.get_time()
        weather = self.get_weather()
        bg, weather_cond = self.get_image(weather)
        self.weatherBg = self.create_image(0, 0, image=bg, anchor='nw')
        self.weatherCond = self.create_image(
            160, 120, image=weather_cond, anchor='nw')
        self.time_rectangle = self.create_rectangle(
            3, 3, 263, 50, width=6, outline=self.work_time_color(time))
        self.city = self.create_text(133, 30, text=self.city, font=BIG_FONT)
        self.time = self.create_text(133, 85, text=time, font=TIME_FONT)
        self.temperature = self.create_text(
            60, 150, text=str(weather['temperature'])+'°C', font=BIG_FONT)
        self.feelsLikeTemp = self.create_text(
            60, 190, text=weather['temperature'], font=SMALL_FONT)
        self.windSpeed = self.create_text(
            80, 250, font=SMALL_FONT,
            text=f'{weather["windSpeed"]} м/с,'
                 f' {WIND_DIRECTION[weather["windDirection"]]}')
        self.humidity = self.create_text(
            200, 250, text=str(weather['humidity'])+'%', font=SMALL_FONT)
        self.cloudness = self.create_text(
            200, 220, text=CLOUDINESS[weather['cloudiness']],
            font=SMALLEST_FONT)

    def update_widget(self):
        time = self.get_time()
        weather = self.get_weather()
        bg, weather_cond = self.get_image(weather)
        self.itemconfig(self.time_rectangle,
                        outline=self.work_time_color(time))
        self.itemconfig(self.weatherBg, image=bg)
        self.itemconfig(self.weatherCond, image=weather_cond)
        self.itemconfig(self.time, text=time)
        self.itemconfig(self.temperature,
                        text=str(weather['temperature'])+'°C')
        self.itemconfig(self.feelsLikeTemp, text=weather['temperature'])
        self.itemconfig(self.windSpeed,
                        text=f'{weather["windSpeed"]} м/с,'
                             f' {WIND_DIRECTION[weather["windDirection"]]}')
        self.itemconfig(self.humidity, text=str(weather['humidity'])+'%')
        self.itemconfig(self.cloudness, text=CLOUDINESS[weather['cloudiness']])
        self.after(60000, self.update_widget)


def main():
    for i in range(len(cities)):
        city = cities[i]
        cityCanvas = CityCanvas(root, city[0], city[1], city[2])
        cityCanvas.pack(fill='both', expand=True)
        cityCanvas.place(x=WIDGET_COORDINATES[i][0],
                         y=WIDGET_COORDINATES[i][1])
        citiesCanvases.append(cityCanvas)


def update():
    for i in range(len(cities)):
        city = citiesCanvases[i]
        city.update_widget()
        city.after(60000, city.update_widget)


def shif_newsline():
    shif_newsline.msg = shif_newsline.msg[1:] + shif_newsline.msg[0]
    svar.set(shif_newsline.msg)
    root.after(100, shif_newsline)


main()

shif_newsline.msg = make_newsfeed()
shif_newsline()
labl.place(x=0, y=370, anchor='sw')

update()
root.mainloop()
