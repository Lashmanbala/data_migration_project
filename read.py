import pymysql
from logging_config import logger

def read_table(endpoint, db_name, user_name, password, table_name, limit=0):
    try:
        conn = pymysql.connect( host = endpoint,
                                port = 3306,
                                user = user_name,
                                password = password,
                                database = db_name )
        
        cursor = conn.cursor()

        if limit == 0:
            query = f'SELECT * FROM {table_name};'
        else:
            query = f'SELECT * FROM {table_name} LIMIT {limit};'

        cursor.execute(query)
        logger.info(f'Successfully read data from {table_name}')

        data = cursor.fetchall()
        column_names_query = f'SHOW COLUMNS FROM {table_name};'

        cursor.execute(column_names_query)
        logger.info(f'Successfully read column names of {table_name} table')

        columns = cursor.fetchall()
        column_names = [col[0] for col in columns]    # to be able to build insert query string

        return data, column_names
    
    except Exception as e:
        logger.info(f'Error with exception: {e}')
    finally:
        cursor.close()
        conn.close()