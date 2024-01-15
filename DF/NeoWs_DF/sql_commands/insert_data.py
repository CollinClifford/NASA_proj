import json
import logging

logging.basicConfig(filename='logs/main.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# def insert_data(cursor, data):

#     columns = data.keys()
#     values = [data[column] for column in columns]

#     # Builds insert query
#     insert_query = f"""
#         INSERT INTO neows.neows_raw ({', '.join(columns)})
#         VALUES ({', '.join(['%s' for _ in range(len(columns))])});
#         """

#     cursor.execute(insert_query, values)

def insert_data(cursor, data):
    try:
        date = data['date']
        # Assuming 'data' is the entire nested JSON
        data_json = json.dumps(data)

        # Builds insert query
        insert_query = f"""
            INSERT INTO neows.neows_raw (date, objects)
            VALUES (%s, %s);
        """

        cursor.execute(insert_query, (date, data_json))
    except Exception as e:
        logging.error(f"Error inserting data: {e}")
        logging.error("Data causing the issue:", data)
