# TODO: Will trigger all of the Data Factory pipelines

import subprocess
import os
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

current_directory = os.path.dirname(os.path.abspath(__file__))
apod_df = os.path.join(current_directory, 'APOD_DF/apod_df.py')
neows_df = os.path.join(current_directory, 'NeoWs_DF/neows_df.py')

try:
    subprocess.run(['python', apod_df])
    subprocess.run(['python', neows_df])
except Exception as e:
    logging.error(f'One or more subprocesses failed: {e}')