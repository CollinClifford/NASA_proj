import requests
from datetime import datetime, timedelta
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def return_json(api_key, start_date, end_date, timeframe="current"):
    json = {}
    url = f"https://api.nasa.gov/neo/rest/v1/feed"
        
    if timeframe == "current":
        
        params = {'start_date': start_date, 'end_date': end_date, 'api_key': api_key}

        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                json = response.json()
                return json
            else:
                logging.error(f"Error: {response.status_code}")
        except Exception as e:
                logging.error(f"An error occured: {e}")
    
    if timeframe == "historical":
        
        params = {'start_date': '2020-01-01', 'end_date': '2024-01-01','api_key': api_key}
        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                json = response.json()
                return json
            else:
                logging.error(f"Error: {response.status_code}")
        except Exception as e:
                logging.error(f"An error occured: {e}")