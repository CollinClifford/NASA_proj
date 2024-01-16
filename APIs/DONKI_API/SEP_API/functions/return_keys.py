import json
import os
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_keys_from_json(json_file_path):
    keys_array = []

    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data_list = json.load(file)

            if isinstance(data_list, list):
                for data in data_list:
                    if isinstance(data, dict):
                        for key in data.keys():
                            keys_array.append(key)
                    else:
                        logging.info("JSON file should contain a list of dictionaries.")
            else:
                logging.info("JSON file should contain a list of dictionaries.")

    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        logging.error(f"Error loading JSON file: {e}")

    keys_array = list(set(keys_array))

    return keys_array

current_script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.abspath(os.path.join(current_script_directory, '..', '..'))
json_file_path = os.path.join(project_directory, 'SEP_API/JSON_data/SEP.json')

keys_array = extract_keys_from_json(json_file_path)

print(keys_array)
