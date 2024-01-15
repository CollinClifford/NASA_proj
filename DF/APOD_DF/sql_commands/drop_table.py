def drop_table(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS apod.apod_raw;
    """
    cursor.execute(drop_table_query)