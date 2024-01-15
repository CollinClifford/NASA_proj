import requests
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def return_json(api_key, timeframe="current"):
    json = {}
    url = "https://api.nasa.gov/planetary/apod"

    if timeframe == "current":
        
        params = {'api_key': api_key, 'thumbs': 'True'}

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
        
        params = {'api_key': api_key, 'thumbs': 'True', 'start_date': '2024-01-01'}
        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:
                json = response.json()
                return json
            else:
                logging.error(f"Error: {response.status_code}")
        except Exception as e:
                logging.error(f"An error occured: {e}")