def drop_table(cursor):
    drop_table_query = """
    DROP TABLE IF EXISTS neows.neows_raw;
    """
    cursor.execute(drop_table_query)