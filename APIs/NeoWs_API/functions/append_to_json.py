import os
import json
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def append_to_json(data):

    existing_data = []

    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.abspath(os.path.join(current_script_directory, '..', '..'))
    json_file_path = os.path.join(project_directory, 'NeoWs_API/JSON_data/neows.json')

    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        logging.error(f"Error loading existing data: {e}")

    if 'near_earth_objects' in data:
        neo_objects = data['near_earth_objects']

        for date, objects_list in neo_objects.items():
            existing_dates = [entry.get('date') for entry in existing_data]
            if date not in existing_dates:
                existing_data.append({'date': date, 'objects': objects_list})
                logging.info(f"Data for date {date} appended successfully.")
            else:
                logging.info(f"Data for date {date} already exists. Skipping append.")
    else:
        logging.error("Error: 'near_earth_objects' key not found in the provided data.")

    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, indent=2)