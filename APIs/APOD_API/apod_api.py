import os
from dotenv import load_dotenv
from functions.return_json import return_json
from functions.append_to_json import append_to_json
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

timeframe="historical"

if __name__ == "__main__":
    try:
        api_key = os.getenv('API_KEY')
    except Exception as e:
        logging.error(f"API key not found: {e}")

    try: 
        data_json = return_json(api_key, timeframe=timeframe)
    except Exception as e:
        logging.error(f"return_json function misfired: {e}")

    try:
        if timeframe == "historical":
            for entry in data_json:
                append_to_json(entry)
        else:
            append_to_json(data_json)
    except Exception as e:
        logging.error(f"append_json function misfired: {e}")