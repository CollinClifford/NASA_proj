def create_table(cursor):
    create_table_query = """
    CREATE TABLE apod.apod_raw (
    id SERIAL PRIMARY KEY,
    service_version text,
    media_type text,
    hdurl text,
    title text,
    copyright text,
    url text,
    date date UNIQUE,
    explanation text,
    thumbnail_url text
    )
    """
    
    cursor.execute(create_table_query)