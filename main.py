# TODO: This will trigger the entire operation.
# TODO: It will run in the following order:
# TODO: 1. APIs
# TODO: 2. Data Factory
# TODO: 3. Stored Procedures
# TODO: Need to consider how this will be an active server

import logging
import subprocess
import os

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Trigger APIs

current_directory = os.path.dirname(os.path.abspath(__file__))
all_apis = os.path.join(current_directory, 'APIs/main.py')

try:
    subprocess.run(['python', all_apis])
except Exception as e:
    logging.error(f'One or more subprocesses failed: {e}')

# Trigger Data Factory

current_directory = os.path.dirname(os.path.abspath(__file__))
all_df = os.path.join(current_directory, 'DF/main.py')

try:
    subprocess.run(['python', all_df])
except Exception as e:
    logging.error(f'One or more subprocesses failed: {e}')