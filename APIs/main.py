# TODO: This file will gather and run all of the APIs daily.

import subprocess
import os
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

current_directory = os.path.dirname(os.path.abspath(__file__))
apod_api = os.path.join(current_directory, 'APOD_API/apod_api.py')
neows_api = os.path.join(current_directory, 'NeoWs_API/neows_api.py')
donki_api = os.path.join(current_directory, 'DONKI_API/donki_api.py')

try:
    subprocess.run(['python', apod_api])
    subprocess.run(['python', neows_api])
    subprocess.run(['python', donki_api])
except Exception as e:
    logging.error(f'One or more subprocesses failed: {e}')
