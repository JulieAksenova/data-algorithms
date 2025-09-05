# etl.py 
# This script extracts weather data from OpenWeatherMap API,
# transforms it into a structured format, and loads it into Postgres.

import requests
import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, timedelta


DB_CONFIG = {
     "dbname": "bdStudy",
     "user": "yuliaaksenova",
     "password": "Tom_clancy9",
     "host": "localhost",
     "port": 5432
}

API_KEY = "812c2a76fdadee355f3f42bbcc6bb8a"
LAT = 39.2776
LON = -74.5746


def extract():
    url = "http://api.openweathermap.org/data/2.5/weather?q=Ocean%20City,NJ,US&appid=8812c2a76fdadee355f3f42bbcc6bb8a&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def extract_1():
     for i in range(1, 4):
          dt = int((datetime.utcnow() - timedelta(days=i)).timestamp())
          url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine"
          params = {
               "lat": LAT,
               "lon": LON,
               "dt": dt,
               "appid": API_KEY,
               "units": "metric"
          }
          r =requests.get(url, params=params)
          print(r.json())


def transform(data_json):
        transformed = {
             "city": data_json.get("name"),
             "temperature": data_json["main"]["temp"],
             "humidity": data_json["main"]["humidity"],
             "wind_speed": data_json["wind"]["speed"],
             "datetime": datetime.datetime.fromtimestamp(data_json["dt"])      
        }
        return transformed

def load(transformed_data):
     conn = psycopg2.connect(**DB_CONFIG)
     cursor = conn.cursor()
     cursor.execute("""
          INSERT INTO weather_params(city, temp, humid, wind_speed, datetime)
          VALUES (%s, %s, %s, %s, %s)
     """, (
          transformed_data["city"],
          transformed_data["temperature"],
          transformed_data["humidity"],
          transformed_data["wind_speed"],
          transformed_data["datetime"]
     ))
     conn.commit()
     cursor.close()
     conn.close()


     print("Test")



def main():
    data = extract()
    data_transformed = transform(data)
    ##load(data_transformed)
    print(data)
    print(data_transformed)
    print(f"Weather data for {data_transformed['city']} successfully loaded into Postgres!")

if __name__ == "__main__":
     main()