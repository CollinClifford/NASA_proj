import psycopg2
import json
from dotenv import load_dotenv
import os
from sql_commands.create_table import create_table
from sql_commands.insert_data import insert_data
from sql_commands.drop_table import drop_table
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():

    load_dotenv()
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    ssl_mode = os.getenv("SSL_MODE")

    db_params = {
        'host': db_host,
        'database': db_name,
        'user': db_user,
        'password': db_password,
        'port': db_port,
        'sslmode': ssl_mode
    }

    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.abspath(os.path.join(current_script_directory, '..', '..'))
    json_file_path = os.path.join(project_directory, 'APIs/APOD_API/JSON_data/apod.json')

    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)
        
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        drop_table(cursor)

        create_table(cursor)

        for record in json_data:
            insert_data(cursor, record)

        conn.commit()
        conn.close()

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
