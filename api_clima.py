import pandas as pd
import requests
from tqdm import tqdm

from twilio_config import API_KEY_WAPI

# método para ubicación (Toma la IP de quien consulta) documentación -> https://www.weatherapi.com/docs/#apis-forecast
query = 'auto:ip'
api_key = API_KEY_WAPI

# URL de la API.
url_clima = 'http://api.weatherapi.com/v1/forecast.json?key=' + api_key + '&q=' + query + '&lang=es&days=1&aqi=no&alerts=no'

# GET al url con el modulo request. docs -> https://requests.readthedocs.io/en/latest/
response = requests.get(url_clima).json()
keys = response.keys()

# keys generales de location.
location = response['location']
localtime = location['localtime']

# keys generales de forecastday.
forecastday = response['forecast']['forecastday'][0]

# keys generales de day.
day = forecastday['day']

# Recorte de algunas keys en day.
max_temp = day['maxtemp_c']
min_temp = day['mintemp_c']
condicion = day['condition']['text']

# Dentro del key "hour".
hour = forecastday['hour']

# ----- Data Frame ------
datos = []
colxl = ["Fecha", "Hora", "Condición", "Temperatura", "Viento", "Dirección", "Humedad", "Llueve",
         "Probabilidad de Lluvia"]

col = ["Hora", "Condición", "Temperatura", "Humedad"]


def pronosticoxl(response, i):
    fecha = localtime.split()[0]
    tiempo = hour[i]['time']
    reloj = tiempo.split()[1]
    hora = reloj.split(':')[0]
    estado = hour[i]['condition']['text']
    temp_c = hour[i]['temp_c']
    wind = hour[i]['wind_kph']
    wind_dir = hour[i]['wind_dir']
    humidity = hour[i]['humidity']
    rain = hour[i]['will_it_rain']
    chance_of_rain = hour[i]['chance_of_rain']

    return fecha, hora, estado, temp_c, wind, wind_dir, humidity, rain, chance_of_rain


def pronostico(response, i):
    tiempo = hour[i]['time']
    reloj = tiempo.split()[1]
    hora = reloj.split(':')[0]
    estado = hour[i]['condition']['text']
    temp_c = hour[i]['temp_c']
    humidity = hour[i]['humidity']

    return hora, estado, temp_c, humidity


for i in tqdm(range(len(hour)), colour='green'):
    datos.append(pronosticoxl(hour, i))

df = pd.DataFrame(datos, columns=colxl)

df_rain = df[(df['Llueve'] == 1)]
df_rain = df_rain[["Hora", "Condición"]]

print(df_rain)
