def select_all(cursor):
    select_all_query="""
SELECT * FROM neows.neows_raw;
"""
    cursor.execute(select_all_query)