def select_all(cursor):
    select_all_query="""
SELECT * FROM apod.apod_raw;
"""
    cursor.execute(select_all_query)