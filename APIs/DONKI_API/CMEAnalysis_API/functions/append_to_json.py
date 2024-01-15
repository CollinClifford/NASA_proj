import os
import json
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def append_to_json(data):
    
    existing_data = []

    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.abspath(os.path.join(current_script_directory, '..', '..'))
    json_file_path = os.path.join(project_directory, 'CMEAnalysis_API/JSON_data/cme_analysis.json')
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        logging.error(f"Error loading existing data: {e}")

    existing_dates = [entry.get('time21_5') for entry in existing_data]
    if data['time21_5'] not in existing_dates:
        existing_data.append(data)
        with open(json_file_path, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, indent=2)
        logging.info("Data appended successfully.")
    else:
        logging.info(f"Data with date {data['time21_5']} already exists. Skipping append.")