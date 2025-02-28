import requests
import time
import random
from smbus2 import SMBus
from bmp280 import BMP280

# ThingSpeak API kulcs
API_KEY = 'HX1HIJ1Y9Q6CMGTV'

# Adatok küldése a ThingSpeak-re
def send_data_to_thingspeak(temp, humidity):
    url = f'https://api.thingspeak.com/update?api_key={API_KEY}&field1={temp}&field2={pressure}'
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Sikeres adatküldés: Hőmérséklet={temp}, Légnyomás={humidity}")
    else:
        print(f"Sikertelen adatküldés: {response.status_code}")

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

# Végtelen ciklus 10 másodperces időközönként
while True:
    
    # Véletlenszerű hőmérséklet és páratartalom generálása
    #temperature = round(random.uniform(20.0, 30.0), 2)  # Példa: 20-30°C között
    #humidity = round(random.uniform(30.0, 70.0), 2)     # Példa: 30-70% között

    #SMB280 sensor adatainak bekérése
    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()
    print(f"{temperature:05.2f}*C {pressure:05.2f}hPa")
    
    # Adatok küldése
    send_data_to_thingspeak(temperature, pressure)
    
    # 10 másodperces várakozás
    time.sleep(10)
