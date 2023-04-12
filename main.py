import requests

import datetime

import sqlite3





url = 'https://www.gismeteo.ru/weather-moscow-4368/'
response = requests.get(url)
if response.status_code == 200:
    html = response.text





    start = html.find('class="unit unit_temperature_c"') + 39
    end = html.find('</span>', start)
    temperature = int(html[start:end])


    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()





    cursor.execute('''CREATE TABLE IF NOT EXISTS weather

                      (date text, time text, temperature integer)''')


    date = datetime.datetime.now().strftime('%Y-%m-%d')
    time = datetime.datetime.now().strftime('%H:%M:%S')





    cursor.execute("INSERT INTO weather VALUES (?, ?, ?)", (date, time, temperature))
    conn.commit()





    print(f'Температура в Москве: {temperature}°C')
    print(f'Данные сохранены в БД: {date} {time}')

else:

    print('Ошибка при получении данных о погоде')