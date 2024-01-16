import os
from dotenv import load_dotenv
from functions.return_json import return_json
from functions.append_to_json import append_to_json
from datetime import datetime, timedelta
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

timeframe=""

if __name__ == "__main__":
    try:
        api_key = os.getenv('API_KEY')
    except Exception as e:
        logging.error(f"API key not found: {e}")

    last_week = datetime.now()
    today = datetime.now()
    count = 1

    while count > 0:
        last_week = datetime.now() - timedelta(30)
        today = datetime.now()
        start_date = "2024-01-01" # last_week.strftime("%Y-%m-%d")
        end_date = today.strftime("%Y-%m-%d")
        try: 
            data_json = return_json(api_key, start_date, end_date)

        except Exception as e:
            logging.error(f"return_json function misfired: {e}")

        try:
            for entry in data_json:
                append_to_json(entry)
        except Exception as e:
            logging.error(f"append_json function misfired: {e}")
        count = count -1