import psycopg2
import os
from logging_config import logger

def build_insert_query(tabl_name, columns):
    try:
        columns_str = ', '.join(columns)
        column_value_placeholeders = tuple(map(lambda clm : clm.replace(clm, '%s'), columns))
        column_value_placeholeders_str = ', '.join(column_value_placeholeders)
        query = f'INSERT INTO {tabl_name} ({columns_str}) VALUES ({column_value_placeholeders_str})'
        return query
    except Exception as e:
        logger.error(f'Error while building query string: {e}')

        
def load_table(endpoint, db_name, user_name, password, table_name, columns, data, batch_size=100):
    try:
        conn = psycopg2.connect( host = endpoint,
                                 port = 5432,
                                 user = user_name,
                                 password = password,
                                 database = db_name )
        cursor = conn.cursor()

        query = build_insert_query(table_name, columns)

        records = []
        counter = 1
        for rec in data:
            records.append(rec)
            if counter % batch_size == 0:
                cursor.executemany(query, records)
                conn.commit()
                logger.info(f'Successfully loaded batch {counter} of {table_name}')
                records = []
            counter += 1
        cursor.executemany(query, records)  # for the last batch of data which is lesser than batch_size
        conn.commit()
        logger.info(f'Successfully loaded batch {counter} of {table_name}')

    
    except Exception as e:
        logger.error(f'Error with exception: {e}')
    finally:
        cursor.close()
        conn.close()
