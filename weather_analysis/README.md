# Weather ETL Project
## Descriptoon
This project fetches weather data from the OpenWeatherAPI,
transformed it into a structured format, and loads it into a PostgreSQL data base.
It demonstrates an ETL (Extract, Transforme, Load) pipeline using Python.

## Installation

1. Clone this repository:
git clone https://github.com/JulieAksenova/etl-weather-api.git

2. Create a virtual environment and activate it:
python3 -m venv venv_v
source venv_v/bin/activate

3. Install required packages:
pip install -r requirements.txt

## Usage

1. Set your OpenWeatherMap API key:
API_KEY = "your_api_key_here"

2. Run the ETL script:
python etl.py

3. The script will fetch weather data for the specified city,
transform ir, and insert it into your PostgreSQL database.

## Data Source
https://openweathermap.org

## Functions
extract() - Fetches raw data from the API
transform(data_json) - Converts raw data into structured format
load(transformed_data) - Loads data into PostgreSQL

## Author

Aksenova Julie 
julieaksenova@gmail.com