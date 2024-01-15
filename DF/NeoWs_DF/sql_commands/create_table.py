def create_table(cursor):
    create_table_query = """
    CREATE TABLE neows.neows_raw (
    id SERIAL PRIMARY KEY,
    date date UNIQUE,
    objects JSONB
    )
    """
    
    cursor.execute(create_table_query)